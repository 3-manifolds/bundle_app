import os
import shutil
import plistlib
import toml
import subprocess

class AppBundle:

    python_link = '../Frameworks/Python.framework/Versions/Current/bin/python3'

    def __init__(self):
        with open("info.toml") as info_toml:
            self.info = info = toml.load(info_toml)
        self.app_name = info['CFBundleDisplayName']
        self.bundle = self.app_name + '.app'
        self.icon_file = info['CFBundleIconFile']
        self.sdef_file = info['OSAScriptingDefinition']

    def create_bundle_structure(self):
        """Construct a macOS Application bundle.

        The info.toml file provides configuration information.
	This assumes that the current working directory contains:
            A configuration file info.toml.
            A directory main_ex containing the main executable;
            An icon file named as specified in info.toml;
            An sdef file named as specified in info.toml;
            A python script named main.py which runs the app;
            A tarball (or a symlink to one) named Frameworks.tgz.
	"""
        os.chdir('main_ex')
        subprocess.run(['make'])
        os.chdir(os.path.pardir)
        # Raises an exception if the app exists.
        os.mkdir(self.bundle)
        contents = os.path.join(self.bundle, 'Contents')
        macos = os.path.join(contents, 'MacOS')
        resources = os.path.join(contents, 'Resources')
        for subdir in (contents, macos, resources):
            os.makedirs(subdir, exist_ok=True)
        shutil.copy(self.icon_file, resources)
        shutil.copy(self.sdef_file, resources)
        main_ex_path = os.path.join(macos, self.app_name)
        shutil.copy('main_ex/AppMain', main_ex_path)
        plist_path = os.path.join(contents, 'Info.plist')
        with open(plist_path, "wb") as info_plist:
            plistlib.dump(self.info, info_plist)
        symlink_path = os.path.join(macos, 'Python')
        os.symlink(self.python_link, symlink_path)
        shutil.copy('main.py', resources)
        subprocess.run(['tar', 'xz', '-C', contents,
             '-f', 'Frameworks.tgz'])


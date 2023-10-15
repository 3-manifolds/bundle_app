Bundle Up
=========

This python package builds a macOS Application bundle for
a python/tkinter app.  It embeds the frameworks built by
the 3-manifolds frameworks project within the app.

To get started, by building a simple example app, run
this command::

    python3 -m bundle_up.init Silly

This will create a directory named silly which serves
as a development directory for the app.  In particular,
the script main.py is what runs your app.  To create your
silly app, do:

    cd silly
    python3 -m bundle_up.build

When you build your real app you will want to replace
the icon file with one designed for your app and edit
main.py so that it runs your app.  You may create a
Requirements.txt file in the development directory to
specify pypi packages which should be installed within
the embedded python framework.  You may also edit
info.toml and the sdef file to suit your needs. 

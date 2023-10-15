ARCH := $(shell uname -m)
ifeq ($(ARCH),x86_64)
CFLAGS = -mmacos-version-min=10.9
else
CFLAGS = -mmacos-version-min=11.0
endif
AppMain: AppMain.c
	gcc $(CFLAGS) -o AppMain -framework CoreFoundation AppMain.c

#!/usr/bin/env python

import os
import sys
import shutil

from distutils.core import setup
from Cython.Build import cythonize


print "\nInstalling Cython shared objects ...\n" 

args = sys.argv[1:]

# Bgsubtraction module
sys.argv.insert(1, "build_ext")
sys.argv.insert(2, "-i")
sys.argv.insert(3, "clean")


setup(
    ext_modules = cythonize("bgsubtraction/cbackground.pyx")
)

print "Moving bgsubtraction compiled files ..."
os.rename("TFM/bgsubtraction/cbackground.so", "bgsubtraction/cbackground.so")

print "Removing bgsubtraction compiled files ..."
os.remove("bgsubtraction/cbackground.c")
shutil.rmtree('TFM/')

print "Setup done\n"
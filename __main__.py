#!/usr/bin/env python

"""
Main process of the project
"""

from __init__ import initvariables
from threedgeometry.loadgrazptz1 import loadcalibration, getcam1

initvariables()
loadcalibration()
a = getcam1()
a.printcamerainfo()


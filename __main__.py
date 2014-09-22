#!/usr/bin/env python

"""
Main process of the project
"""

from __init__ import initvariables
from threedgeometry.loadgrazptz1 import loadcalibration, setglobalvariables
from threedgeometry.video import Video

initvariables()
setglobalvariables()
loadcalibration()
a = Video()
a.readvideo()



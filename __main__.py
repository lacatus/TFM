#!/usr/bin/env python

"""
Main process of the project
"""

from __init__ import init
from datasets import loadgrazptz1

init()
loadgrazptz1.loaddataset()
loadgrazptz1.printcamerainfo()




#!/usr/bin/env python

"""
Main process of the project
"""

from __init__ import init
from datasets import icglab1
from datasets import loadgrazptz1
from datasets import loadgrazptz2

init()
icglab1.loaddataset()
icglab1.printcamerainfo()




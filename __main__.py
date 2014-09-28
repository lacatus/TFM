#!/usr/bin/env python

"""
Main process of the project
"""

# Initialization
from __init__ import init

# Datasets imports
import datasets.datasetloader
import datasets.grazptz1
import datasets.grazptz2
import datasets.icglab1
import datasets.icglab2
import datasets.icglab3
import datasets.icglab4
import datasets.icglab5
import datasets.icglab6

# Modules imports
from var import variables

init()
dataset = datasets.datasetloader.selectdataset()
e = 'datasets.%s.loaddataset()' % dataset
cams = eval(e)





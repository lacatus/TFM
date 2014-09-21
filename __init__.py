#!/usr/bin/env python

"""
Initialization of the project global variables
"""

import os

from var import variables


def initvariables():

    variables.app_path = os.path.dirname(os.path.realpath(__file__))
    variables.datasets_path = variables.app_path + '\data'

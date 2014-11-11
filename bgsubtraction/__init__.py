#!/usr/bin/env python

"""
The scripts that compose this module contains a set of functions
needed to process properly a background subtraction of each camera
of a dataset
"""

import cbackground
import cv2
import numpy as np
import sys

from gui import trackbar
from threedgeometry import frameretriever

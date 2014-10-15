#!/usr/bin/env python

"""
The functions that compose this module try to give a solution to the
3d geometry transformations that the OpenCV 3dcalib module does not
offer. Specifically the ones that refer to the retroprojection of points
from the 2d to the 3d plane with ground plane (z) equal to 0.

Also a different implementation of the camera calibration class is
offered in a much simpler way. This will allow to load the proper values
of the camera in a much simpler way through the Configuration Parser
option that Python offers.
"""

import os
import cv2

import ConfigParser as cp
import numpy as np

from var import variables

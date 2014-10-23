#!/usr/bin/env python

"""
Initialization of the project global variables
"""

import cv2
import os

from var import variables


def init():

    initvariables()


def initvariables():

    variables.app_path = os.path.dirname(os.path.realpath(__file__))
    variables.datasets_path = variables.app_path + '/data'

    variables.datasets_name = {
        1: 'grazptz1',
        2: 'grazptz2',
        3: 'icglab1',
        4: 'icglab2',
        5: 'icglab3',
        6: 'icglab4',
        7: 'icglab5',
        8: 'icglab6',
        9: 'pets091',
        10: 'pets092',
        11: 'pets093',
        12: 'pets094',
        13: 'pets095',
        14: 'pets096',
        15: 'pets097',
        16: 'pets098',
        17: 'pets099'}

    variables.app_window_name = 'Main Window'
    variables.app_window = cv2.namedWindow(
        variables.app_window_name, cv2.WINDOW_NORMAL)

    variables.app_window_trackbar_name = 'Main Background Window'
    variables.app_window_trackbar = cv2.namedWindow(
        variables.app_window_trackbar_name, cv2.WINDOW_NORMAL)

    variables.app_window_trackbar_name_2 = 'Secondary Background Window'
    variables.app_window_trackbar_2 = cv2.namedWindow(
        variables.app_window_trackbar_name_2, cv2.WINDOW_NORMAL)

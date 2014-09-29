#!/usr/bin/env python

from bgsubtraction import cv2
from bgsubtraction import np

# TODO --> read description
"""
Implement the main methods for the background subtraction modelling.
1. Main BG subtraction
2. Scanning window
3. Different threshold methods
4. Window agroupation ?? --> Maybe GUI module
"""


class Bg(object):

    """
    Parent class of the Background class that contains common
    attributes shared by every Background object
    """

    def __init__(self):

        self.alpha = None
        self.beta = None
        self.counter = None
        self.frame_count = None
        self.threshold_1 = None
        self.threshold_2 = None

    def setdefault(self):

        self.alpha = 0.9
        self.beta = 0.1
        self.counter = 1
        self.frame_count = 30
        self.threshold_1 = 5
        self.threshold_2 = 25


class Background(Bg):

    """
    Background class contains the different parameters and
    attributes the application background model needs.This
    object is intended to be adaptable for each camera view.
    """

    def __init__(self, bg):

        self.bg = bg
        self.win_height = None
        self.win_width = None
        self.win_min_pix = None
        self.bg_img = None
        self.bin = None  # TODO --> how to get binary image

    def setdefault(self, bg_img):

        self.win_height = 30
        self.win_width = 15
        self.win_min_pix = 200 * 255  # 255 or 0 --> how a white pixel counts in b/w img
        self.bg_img = bg_img

        #height, width, depth = bg_img.shape
        #self.bin = np.zeros()

    def updatebackground(self, bg_img):

        if self.bg_img.any():

            if self.bg.frame_count is self.bg.counter:
                dst = cv2.addWeighted(self.bg_img, self.bg.alpha, bg_img, self.bg.beta, 0)
                self.bg_img = dst
                # TODO --> Fix no bg update
                self.bg.counter = 1

            else:
                self.bg.counter += 1

        else:
            raise Exception('Background model parameters not initialized \n '
                            'Please initiatilize parameters with setdefault() function')
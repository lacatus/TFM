#!/usr/bin/env python

from bgsubtraction import cv2
from bgsubtraction import np

# TODO --> read description
"""
Implement the main methods for the background subtraction modelling.
2. Scanning window
3. Different threshold methods
"""


class Bg(object):

    """
    Parent class of the Background class that contains common
    attributes shared by every Background object
    """

    def __init__(self):

        self.alpha = None
        self.beta = None
        self.frame_count = None
        self.threshold_1 = None
        self.threshold_2 = None

    def setdefault(self):

        self.alpha = 0.9
        self.beta = 0.1
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
        self.counter = None
        self.win_height = None
        self.win_width = None
        self.win_min_pix = None
        self.bg_img = None
        self.bin_img = None

    def setdefault(self, bg_img):

        size = bg_img.shape
        height = size[0]
        width = size[1]

        if len(size) < 3:
            self.counter = 1
            self.win_height = 30
            self.win_width = 15
            self.win_min_pix = 200 * 255  # 255 or 0 --> how a white pixel counts in b/w img
            self.bg_img = bg_img
            self.bin_img = np.zeros((height, width))

        else:
            raise Exception('Background model parameters incorrectly initialized \n '
                            'Please initiatilize parameters with a gray scale image')

    def updatebackground(self, bg_img):

        if self.bg_img.any():

            if self.bg.frame_count is self.counter:
                self.bg_img = cv2.addWeighted(self.bg_img, self.bg.alpha, bg_img, self.bg.beta, 0)
                self.counter = 1

            else:
                self.counter += 1

        else:
            raise Exception('Background model parameters not initialized \n '
                            'Please initiatilize parameters with setdefault() function')

    def subtractbackground(self, bg_img):

        if self.bg_img.any():
            self.bin_img = cv2.subtract(self.bg_img, bg_img)
            ret, self.bin_img = cv2.threshold(self.bin_img, self.bg.threshold_1, 255, cv2.THRESH_BINARY)

        else:
            raise Exception('Background model parameters not initialized \n '
                            'Please initiatilize parameters with setdefault() function')
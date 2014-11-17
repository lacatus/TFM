#!/usr/bin/env python

from bgsubtraction import cbackground
from bgsubtraction import cv2
from bgsubtraction import np


class Bg(object):

    """
    Parent class of the Background class that contains common
    attributes shared by every Background object
    """

    def __init__(self):

        self.option = None
        self.alpha = None
        self.beta = None
        self.frame_count = None
        self.threshold_1 = None
        self.threshold_2 = None

    def setdefault(self):

        self.option = 0
        self.alpha = 0.9
        self.beta = 0.1
        self.frame_count = 30
        self.threshold_1 = 25
        self.threshold_2 = 5

    def setconfiguration(self, config):

        self.option = config['option']
        self.alpha = config['option']
        self.beta = config['beta']
        self.frame_count = config['frame_count']
        self.threshold_1 = config['threshold_1']
        self.threshold_2 = config['threshold_2']


class Background(object):

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
        self.bin_img_2 = None
        self.scan_img = None
        self.diff_img = None
        self.contours = None
        self.rectangles = None

    def setdefault(self, src):

        size = src.shape
        height = size[0]
        width = size[1]

        self.counter = 1
        self.win_height = 30
        self.win_width = 15
        self.win_min_pix = 200
        self.bg_img = src
        self.bin_img_1 = np.zeros((height, width))
        self.bin_img_2 = self.bin_img
        self.scan_img = self.bin_img
        self.diff_img = self.bin_img
        self.diff_img_copy = self.bin_img
        self.contours = None
        self.rectangles = []

    def setconfiguration(self, src, config):

        size = src.shape
        height = size[0]
        width = size[1]

        self.counter = 1
        self.win_height = config['win_height']
        self.win_width = config['win_width']
        self.win_min_pix = config['win_min_pix']
        self.bg_img = src
        self.bin_img_1 = np.zeros((height, width))
        self.bin_img_2 = self.bin_img
        self.scan_img = self.bin_img
        self.diff_img = self.bin_img
        self.diff_img_copy = self.bin_img
        self.contours = None
        self.rectangles = []

    def updatebackground(self, src):

        if self.bg_img.any():
            if self.bg.frame_count is self.counter:

                self.bg_img = cv2.addWeighted(
                    self.bg_img, self.bg.alpha, src, self.bg.beta, 0)
                self.counter = 1

            else:
                self.counter += 1

        else:
            raise Exception('Background model parameters not initialized \n '
                            'Please initiatilize parameters with '
                            'setdefault() function')

    def subtractbackground(self, src):

        subtract = cv2.subtract(self.bg_img, src)
        self.bin_img_1 = self._thresholdbackground(
            subtract, self.bg.threshold_1)
        self.bin_img_2 = self._thresholdbackground(
            subtract, self.bg.threshold_2)

    def _thresholdbackground(self, src, threshold):

        ret, threshold_0 = cv2.threshold(
            src[:, :, 0], threshold, 255, cv2.THRESH_BINARY)
        ret, threshold_1 = cv2.threshold(
            src[:, :, 1], threshold, 255, cv2.THRESH_BINARY)
        ret, threshold_2 = cv2.threshold(
            src[:, :, 2], threshold, 255, cv2.THRESH_BINARY)

        return cv2.add(threshold_0.astype(np.uint8), cv2.add(
            threshold_1.astype(np.uint8), threshold_2.astype(np.uint8)))

    def windowscanbackground(self):

        int_img = cv2.integral(self.bin_img_1)
        self.scan_img = cbackground.scanningwindow(
            int_img, self.win_height, self.win_width, self.win_min_pix)

    def thresholdbackground(self):

        self.diff_img = cv2.multiply(self.bin_img_2, self.scan_img)
        self.diff_img_copy = self.diff_img.copy()  # For visualization

    def contoursbackground(self):

        self.contours, hierarchy = cv2.findContours(
            self.diff_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        self.rectangles = []
        contours = []

        for cont in self.contours:
            x, y, w, h = cv2.boundingRect(cont)

            if w >= (self.win_width / 2) and h >= (self.win_height / 2):
                self.rectangles.append([x, y, w, h])
                contours.append(cont)

        self.contours = contours

#!/usr/bin/env python

from bgsubtraction import cv2
from bgsubtraction import np


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
        self.bin_img_2 = None
        self.scan_img = None
        self.diff_img = None

    def setdefault(self, src):

        size = src.shape
        height = size[0]
        width = size[1]

        if len(size) < 3:
            self.counter = 1
            self.win_height = 30
            self.win_width = 15
            self.win_min_pix = 200 * 255  # 255 or 0 --> how a white pixel counts in b/w img
            self.bg_img = src
            self.bin_img = np.zeros((height, width))
            self.bin_img_2 = self.bin_img
            self.scan_img = self.bin_img
            self.diff_img = self.bin_img

        else:
            raise Exception('Background model parameters incorrectly initialized \n '
                            'Please initiatilize parameters with a gray scale image')

    def updatebackground(self, src):

        if self.bg_img.any():

            if self.bg.frame_count is self.counter:
                self.bg_img = cv2.addWeighted(self.bg_img, self.bg.alpha, src, self.bg.beta, 0)
                self.counter = 1

            else:
                self.counter += 1

        else:
            raise Exception('Background model parameters not initialized \n '
                            'Please initiatilize parameters with setdefault() function')

    def subtractbackground(self, src):

        if self.bg_img.any():
            self.bin_img = cv2.subtract(self.bg_img, src)
            ret, self.bin_img = cv2.threshold(self.bin_img, self.bg.threshold_1, 255, cv2.THRESH_BINARY)
            ret, self.bin_img_2 = cv2.threshold(self.bin_img, self.bg.threshold_2, 255, cv2.THRESH_BINARY)

        else:
            raise Exception('Background model parameters not initialized \n '
                            'Please initiatilize parameters with setdefault() function')

    def windowscanbackground(self):

        if self.bin_img.any():
            int_img = cv2.integral(self.bin_img)
            self.scan_img = self._scanningwindow(int_img)

        else:
            raise Exception('Background model images not updated \n '
                            'Please update model images with subtractbackground() function')

    def _scanningwindow(self, src):

        # SRC = Integral image
        # Maybe Cython

        size = src.shape

        height = size[0]
        width = size[1]

        dst = np.zeros((height, width))

        for jj in xrange(0, height - self.win_height, self.win_height / 2):

            for ii in xrange(0, width - self.win_width, self.win_width / 2):

                aux = src[jj, ii] + src[jj + self.win_height, ii + self.win_width] - src[jj + self.win_height, ii] - src[jj, ii + self.win_width]

                if aux > self.win_min_pix:

                    dst[jj : jj + self.win_height, ii : ii + self.win_width] = 255

        return dst

    def thresholdbackground(self):

        if self.bin_img.any():
            self.diff_img = np.multiply(self.bg.threshold_2, self.scan_img)

        else:
            raise Exception('Background model images not updated \n '
                            'Please update model images with subtractbackground() function')
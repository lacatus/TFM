#!/usr/bin/env python

from gui import cv2
from gui import variables


class Trackbarmain(object):

    def __init__(self, bg):

        self.bg = bg

    def setdefault(self):

        cv2.createTrackbar('Option', variables.app_window_trackbar_name,
                           self.bg.option, 5, self.setoption)
        cv2.createTrackbar('Beta', variables.app_window_trackbar_name,
                           int(self.bg.beta * 10), 10, self.setbeta)
        cv2.createTrackbar('Frame Count', variables.app_window_trackbar_name,
                           self.bg.frame_count, 100, self.setframecount)
        cv2.createTrackbar('Threshold 1', variables.app_window_trackbar_name,
                           self.bg.threshold_1, 50, self.setthreshold1)
        cv2.createTrackbar('Threshold 2', variables.app_window_trackbar_name,
                           self.bg.threshold_2, 50, self.setthreshold2)

    def setoption(self, tb_value):
        self.bg.option = tb_value

    def setbeta(self, tb_value):
        self.bg.beta = tb_value / 10.
        self.bg.alpha = 1 - (tb_value / 10.)

    def setframecount(self, tb_value):
        self.bg.frame_count = tb_value

    def setthreshold1(self, tb_value):
        self.bg.threshold_1 = tb_value

    def setthreshold2(self, tb_value):
        self.bg.threshold_2 = tb_value
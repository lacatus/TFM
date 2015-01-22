#!/usr/bin/env python

from gui import cv2
from gui import variables


class TrackbarMain(object):

    def __init__(self, bg):

        self.bg = bg
        self.framebyframe = 0

    def setdefault(self):

        cv2.createTrackbar(
            'Option', variables.app_window_trackbar_name,
            self.bg.option, 9, self.setoption)
        cv2.createTrackbar(
            'Beta', variables.app_window_trackbar_name,
            int(self.bg.beta * 10), 10, self.setbeta)
        cv2.createTrackbar(
            'Frame Count', variables.app_window_trackbar_name,
            self.bg.frame_count, 100, self.setframecount)
        cv2.createTrackbar(
            'Threshold 1', variables.app_window_trackbar_name,
            self.bg.threshold_1, 100, self.setthreshold1)
        cv2.createTrackbar(
            'Threshold 2', variables.app_window_trackbar_name,
            self.bg.threshold_2, 100, self.setthreshold2)
        cv2.createTrackbar(
            'Frame by frame', variables.app_window_trackbar_name,
            self.framebyframe, 1, self.setframebyframe)
        cv2.createTrackbar(
            'Frame Delay', variables.app_window_trackbar_name,
            self.bg.waitkey, 1000, self.setwaitkey)

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

    def setframebyframe(self, tb_value):

        if tb_value is 0:
            self.framebyframe = 0

        if tb_value is 1:
            self.framebyframe = 1

    def setwaitkey(self, tb_value):
        # If 0, then stop and press key
        self.bg.waitkey = tb_value + 1


class TrackbarSecondary(object):

    def __init__(self, background):

        self.background = background

    def setdefault(self, index):

        cv2.createTrackbar(
            'Win Height %s' % str(index), variables.app_window_trackbar_name_2,
            self.background.win_height, 100, self.setwinheight)
        cv2.createTrackbar(
            'Win Width %s' % str(index), variables.app_window_trackbar_name_2,
            self.background.win_width, 100, self.setwinwidth)
        cv2.createTrackbar(
            'Min Pix Win %s' % str(index),
            variables.app_window_trackbar_name_2,
            self.background.win_min_pix, 500, self.setminpixwin)

    def setwinheight(self, tb_value):
        if tb_value < 1:
            self.background.win_height = 1
        else:
            self.background.win_height = tb_value  # Can't be zero

    def setwinwidth(self, tb_value):
        if tb_value < 1:
            self.background.win_width = 1
        else:
            self.background.win_width = tb_value  # Can't be zero

    def setminpixwin(self, tb_value):
        self.background.win_min_pix = tb_value


def setdefaulttrackbarmain(bg):

    tb = TrackbarMain(bg)
    tb.setdefault()

    return tb


def setdefaulttrackbardsecondary(bg_models):

    for ii in range(len(bg_models)):
        tb = TrackbarSecondary(bg_models[ii]).setdefault(ii + 1)

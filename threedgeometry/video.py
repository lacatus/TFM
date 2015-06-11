#!/usr/bin/env python

from threedgeometry import cv2


class Video(object):

    """
    Video class that contains the different values we need to know about
    each video. It also gives the different methods that we need to load
    them and be readable with OpenCV.
    """

    def __init__(self):

        self.id = ''
        self.data = None
        self.width = None
        self.height = None
        # self.fps = None
        self.total_fps = None
        self.bg = None

    def getframe(self):  # returns tuple --> ret, frame

        return self.data.read()

    def getvideoparameters(self):

        """
        # OpenCV 2.4.6
        self.width = self.data.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
        self.height = self.data.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
        # self.fps = self.data.get(cv2.cv.CV_CAP_PROP_FPS)
        self.total_fps = self.data.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
        """
        # OpenCV 3.0.0
        self.width = self.data.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.data.get(cv2.CAP_PROP_FRAME_HEIGHT)
        # self.fps = self.data.get(cv2.cv.CV_CAP_PROP_FPS)
        self.total_fps = self.data.get(cv2.CAP_PROP_FRAME_COUNT)

    def readvideo(self, video_path):

        self.data = cv2.VideoCapture(video_path)
        self.getvideoparameters()

    def readbg(self, bg_path):

        self.bg = cv2.imread(bg_path)

    def printvideoinfo(self):

        print '* Video Parameters *'
        print 'width:\n%s\n%s' % (self.width, type(self.width))
        print 'height:\n%s\n%s' % (self.height, type(self.height))
        # print 'fps:\n%s\n%s' % (self.fps, type(self.fps))
        print 'total_fps:\n%s\n%s' % (self.total_fps, type(self.total_fps))
        print ''

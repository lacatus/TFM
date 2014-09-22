#!/usr/bin/env python

from threedgeometry import cv2
from threedgeometry import variables


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
        self.fps = None
        self.total_fps = None

    def getvideoparameters(self):

        self.width = self.data.get(50)
        print self.width

    def readvideo(self):

        video_path = variables.current_video_path + '\cam-131.avi'
        print video_path
        print cv2.VideoCapture(0).get(3)
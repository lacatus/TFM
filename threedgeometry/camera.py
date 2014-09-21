#!/usr/bin/env python

from threedgeometry import cp
from threedgeometry import np


class Camera(object):

    """
    Camera class that contains the different values we need to know about
    each camera. It also gives the different methods that we need to load
    all the values of each cameras from configuration files.
    """

    def __init__(self):

        # Camera Info
        self.id = ''
        self.model = ''
        self.encoder = ''

        # Camera Parameters
        self.width = None
        self.height = None
        self.frame_rate = None
        self.intrinsics = None
        self.rotation = None
        self.translation = None

    def __formatintegers(self, width, height, frame_rate):

        self.width = int(width)
        self.height = int(height)
        self.frame_rate = int(frame_rate)

    def __formatintrinsics(self, intrinsics):

        m_str = '%s %s %s; %s %s %s; %s %s %s'\
                % (intrinsics[0], intrinsics[1], intrinsics[2],
                   intrinsics[3], intrinsics[4], intrinsics[5],
                   intrinsics[6], intrinsics[7], intrinsics[8])

        self.intrinsics = np.matrix(m_str)

    def __formatrotation(self, rotation):

        m_str = '%s %s %s; %s %s %s; %s %s %s'\
                % (rotation[0], rotation[1], rotation[2],
                   rotation[3], rotation[4], rotation[5],
                   rotation[6], rotation[7], rotation[8])

        self.rotation = np.matrix(m_str)

    def __formattranslation(self, translation):

        m_str = '%s; %s; %s'\
                % (translation[0], translation[1], translation[2])

        self.translation = np.matrix(m_str)

    def readconfigfile(self, config_file):

        c = cp.ConfigParser()
        c.read(config_file)

        self.id = c.get('CameraInfo', 'id')
        self.model = c.get('CameraInfo', 'model')
        self.encoder = c.get('CameraInfo', 'encoder')

        width = c.get('CameraParameters', 'width')
        height = c.get('CameraParameters', 'height')
        frame_rate = c.get('CameraParameters', 'frame_rate')
        intrinsics = c.get('CameraParameters', 'intrinsics').split()
        rotation = c.get('CameraParameters', 'rotation').split()
        translation = c.get('CameraParameters', 'translation').split()

        self.__formatintegers(width, height, frame_rate)
        self.__formatintrinsics(intrinsics)
        self.__formatrotation(rotation)
        self.__formattranslation(translation)

    def printcamerainfo(self):

        print ''
        print 'Printing Camera Object Variables'
        print ''
        print '* Camera Info *'
        print 'id: %s\n%s' % (self.id, type(self.id))
        print 'model: %s\n%s' % (self.model, type(self.model))
        print 'encoder: %s\n%s' % (self.encoder, type(self.encoder))
        print ''
        print '* Camera Parameters *'
        print 'width: %s\n%s' % (self.width, type(self.width))
        print 'height %s\n%s' % (self.height, type(self.height))
        print 'intrinsics:\n%s\n%s' % (self.intrinsics, type(self.intrinsics))
        print 'rotation:\n%s\n%s' % (self.rotation, type(self.rotation))
        print 'translation:\n%s\n%s' % (self.translation, type(self.translation))
        print ''
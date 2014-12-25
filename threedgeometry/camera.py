#!/usr/bin/env python

from threedgeometry import cp
from threedgeometry import cv2
from threedgeometry import np
from threedgeometry.video import Video


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

        # Camera Parameters
        self.intrinsics = None
        self.rotation = None
        self.translation = None
        self.optimalcameramatrix = None
        self.homography = None
        self.inverse_homography = None
        self.roi = None
        self.axis_factor = None
        self.plane = None

        # Video
        self.video = Video()

    def __creategroundplane(self):

        print ''
        print 'Creating world plane for ' + self.id

        a = np.float32([[[0, 0, 0]]])

        for jj in xrange(0, 100, 1):
            for ii in xrange(0, 100, 1):
                    b = np.float32([[[ii - 50, jj - 50, 0]]])
                    a = np.r_[a, b]

        self.plane = a[1:10001]

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

        intrinsics = c.get('CameraParameters', 'intrinsics').split()
        rotation = c.get('CameraParameters', 'rotation').split()
        translation = c.get('CameraParameters', 'translation').split()

        self.axis_factor = c.getint('CameraParameters', 'axis_factor')

        self.__formatintrinsics(intrinsics)
        self.__formatrotation(rotation)
        self.__formattranslation(translation)

        self.__creategroundplane()

        self.initcameracalibration()

    def printcamerainfo(self):

        print ''
        print 'Printing Camera Object Variables'
        print ''
        print '* Camera Info *'
        print 'id: %s\n%s' % (self.id, type(self.id))
        print 'model: %s\n%s' % (self.model, type(self.model))
        print ''
        print '* Camera Parameters *'
        print 'intrinsics:\n%s\n%s' % (self.intrinsics, type(self.intrinsics))
        print 'rotation:\n%s\n%s' % (self.rotation, type(self.rotation))
        print 'translation:\n%s\n%s' % (
            self.translation, type(self.translation))
        print 'homography: \n%s\n%s' % (self.homography, type(self.homography))
        print 'inverse homography: \n%s\n%s' % (
            self.inverse_homography, type(self.inverse_homography))
        print ''

        self.video.printvideoinfo()

    def initcameracalibration(self):

        self.__getoptimalcameramatrix()
        self.__initretroprojection()
        self.__gethomography()

    def __getoptimalcameramatrix(self):

        w = int(self.video.width)
        h = int(self.video.height)

        # http://code.opencv.org/issues/1718
        self.optimalcameramatrix, self.roi = \
            cv2.getOptimalNewCameraMatrix(
                self.intrinsics, np.float64([0, 0, 0, 0]), (w, h), 1, (w, h))

    def __gethomography(self):

        r = self.rotation
        t = self.translation

        h = np.array([
            [r[0, 0], r[0, 1], t[0]],
            [r[1, 0], r[1, 1], t[1]],
            [r[2, 0], r[2, 1], t[2]]
        ])

        self.homography = h / t[2]
        self.inverse_homography = np.linalg.inv(self.homography)

    def __initretroprojection(self):

        # http://bit.ly/opencv2d3d
        r_mat = self.rotation
        t_mat = self.translation

        self.rt = r_mat * t_mat

    def undistortimage(self, ret, src):

        dst = cv2.undistort(
            src, self.intrinsics, None, None, self.optimalcameramatrix)
        x, y, w, h = self.roi

        #return ret, dst[y:y + h, x:x + w]
        return ret, dst

    def getundistortedframe(self):

        ret, frame = self.video.getframe()

        return self.undistortimage(ret, frame)

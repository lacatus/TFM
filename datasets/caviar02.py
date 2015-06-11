#!/usr/bin/env python

from datasets import cp
from datasets import variables
from datasets import Camera


def loaddataset():

    setglobalvariables()
    loadcameras()
    return getcameras(), loadconfiguration()


def setglobalvariables():

    variables.current_dataset_path = variables.datasets_path + '/caviar'
    variables.current_video_path = variables.current_dataset_path + '/videos'


def loadcameras():

    global cam1_g1

    cam1_g1 = Camera()

    #cam1_g1.video.readvideo(variables.current_video_path + '/Meet_WalkTogether1.mpg')
    cam1_g1.video.readvideo(variables.current_video_path + '/Meet_WalkTogether1.avi')

    cam1_g1.video.readbg(
        variables.current_dataset_path + '/background/background.jpg')

    cam1_str = variables.current_dataset_path + '/cameracalib/camera001.cfg'

    cam1_g1.readconfigfile(cam1_str)


def loadglobalconfiguration(c):

    dst = {
        'option': c.getint('global', 'option'),
        'alpha': c.getfloat('global', 'alpha'),
        'beta': c.getfloat('global', 'beta'),
        'frame_count': c.getint('global', 'frame_count'),
        'threshold_1': c.getint('global', 'threshold_1'),
        'threshold_2': c.getint('global', 'threshold_2'),
        'waitkey': c.getint('global', 'waitkey')
    }

    return dst


def loadcamconfiguration(c, cam_id):

    dst = {
        'win_height': c.getint(cam_id, 'win_height'),
        'win_width': c.getint(cam_id, 'win_width'),
        'win_min_pix': c.getint(cam_id, 'win_min_pix')
    }

    return dst


def loadconfiguration():

    config_file = variables.current_dataset_path + '/configuration/config.cfg'

    c = cp.ConfigParser()
    c.read(config_file)

    configuration = {
        'global': loadglobalconfiguration(c),
        'Camera001': loadcamconfiguration(c, 'Camera001'),
        'dir': config_file
    }

    return configuration


def getcam1():

    return cam1_g1


def getcameras():

    cam1 = getcam1()

    cam1.printcamerainfo()

    return [cam1]


def printcamerainfo():

    cam1_g1.printcamerainfo()

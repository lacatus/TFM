#!/usr/bin/env python

from datasets import cp
from datasets import variables
from datasets import Camera


def loaddataset():

    setglobalvariables()
    loadcameras()
    return getcameras(), loadconfiguration()


def setglobalvariables():

    variables.current_dataset_path = variables.datasets_path + '/pets09'
    variables.current_video_path = variables.current_dataset_path + \
        '/s0/citycenter/time_14_55'


def loadcameras():

    global cam1_g1
    global cam2_g1
    global cam3_g1

    cam1_g1 = Camera()
    cam2_g1 = Camera()
    cam3_g1 = Camera()

    cam1_g1.video.readvideo(variables.current_video_path + '/camera001.avi')
    cam2_g1.video.readvideo(variables.current_video_path + '/camera002.avi')
    cam3_g1.video.readvideo(variables.current_video_path + '/camera003.avi')

    cam1_g1.video.readbg(
        variables.current_video_path + '/background/camera001.jpg')
    cam2_g1.video.readbg(
        variables.current_video_path + '/background/camera002.jpg')
    cam3_g1.video.readbg(
        variables.current_video_path + '/background/camera003.jpg')

    cam1_str = variables.current_dataset_path + '/cameracalib/camera001.cfg'
    cam2_str = variables.current_dataset_path + '/cameracalib/camera002.cfg'
    cam3_str = variables.current_dataset_path + '/cameracalib/camera003.cfg'

    cam1_g1.readconfigfile(cam1_str)
    cam2_g1.readconfigfile(cam2_str)
    cam3_g1.readconfigfile(cam3_str)


def loadglobalconfiguration(c):

    dst = {
        'option': c.getint('global', 'option'),
        'alpha': c.getfloat('global', 'alpha'),
        'beta': c.getfloat('global', 'beta'),
        'frame_count': c.getint('global', 'frame_count'),
        'threshold_1': c.getint('global', 'threshold_1'),
        'threshold_2': c.getint('global', 'threshold_2')
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

    config_file = variables.current_video_path + '/configuration/config.cfg'

    c = cp.ConfigParser()
    c.read(config_file)

    configuration = {
        'global': loadglobalconfiguration(c),
        'cam001': loadcamconfiguration(c, 'cam001'),
        'cam002': loadcamconfiguration(c, 'cam002'),
        'cam003': loadcamconfiguration(c, 'cam003'),
        'dir': config_file
    }

    return configuration


def getcam1():

    return cam1_g1


def getcam2():

    return cam2_g1


def getcam3():

    return cam3_g1


def getcameras():

    cam1 = getcam1()
    cam2 = getcam2()
    cam3 = getcam3()

    cam1.printcamerainfo()
    cam2.printcamerainfo()
    cam3.printcamerainfo()

    return [cam1, cam2, cam3]


def printcamerainfo():

    cam1_g1.printcamerainfo()
    cam2_g1.printcamerainfo()
    cam3_g1.printcamerainfo()

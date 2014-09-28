#!/usr/bin/env python

from datasets import variables
from datasets import Camera


def loaddataset():

    setglobalvariables()
    loadcameras()


def setglobalvariables():

    variables.current_dataset_path = variables.datasets_path + '/icglab6'
    variables.current_video_path = variables.current_dataset_path + '/videos/chap'


def loadcameras():

    global cam1_g1
    global cam2_g1
    global cam3_g1
    global cam4_g1

    cam1_g1 = Camera()
    cam2_g1 = Camera()
    cam3_g1 = Camera()
    cam4_g1 = Camera()

    cam1_str = variables.current_dataset_path + '/cameracalib/camera001.cfg'
    cam2_str = variables.current_dataset_path + '/cameracalib/camera002.cfg'
    cam3_str = variables.current_dataset_path + '/cameracalib/camera003.cfg'
    cam4_str = variables.current_dataset_path + '/cameracalib/camera004.cfg'

    cam1_g1.readconfigfile(cam1_str)
    cam2_g1.readconfigfile(cam2_str)
    cam3_g1.readconfigfile(cam3_str)
    cam4_g1.readconfigfile(cam4_str)

    cam1_g1.data.readvideo(variables.current_video_path + '/cam131.avi')
    cam2_g1.data.readvideo(variables.current_video_path + '/cam132.avi')
    cam3_g1.data.readvideo(variables.current_video_path + '/cam133.avi')
    cam4_g1.data.readvideo(variables.current_video_path + '/cam134.avi')


def getcam1():

    return cam1_g1


def getcam2():

    return cam2_g1


def getcam3():

    return cam3_g1


def getcam4():

    return cam4_g1


def printcamerainfo():

    cam1_g1.printcamerainfo()
    cam2_g1.printcamerainfo()
    cam3_g1.printcamerainfo()
    cam4_g1.printcamerainfo()

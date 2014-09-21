#!/usr/bin/env python

from camera import Camera
from threedgeometry import variables


def loadcalibration():

    global cam1_g1
    global cam2_g1
    global cam3_g1

    # Set path for current dataset
    variables.current_dataset_path = variables.datasets_path + '\grazptz\set1'

    cam1_g1 = Camera()
    cam2_g1 = Camera()
    cam3_g1 = Camera()

    cam1_str = variables.current_dataset_path + '\cameracalib\camera001.cfg'
    cam2_str = variables.current_dataset_path + '\cameracalib\camera002.cfg'
    cam3_str = variables.current_dataset_path + '\cameracalib\camera003.cfg'

    cam1_g1.readconfigfile(cam1_str)
    cam2_g1.readconfigfile(cam2_str)
    cam3_g1.readconfigfile(cam3_str)


def getcam1():

    return cam1_g1


def getcam2():

    return cam2_g1


def getcam3():

    return cam2_g1


def printcamerainfo():

    cam1_g1.printcamerainfo()
    cam2_g1.printcamerainfo()
    cam3_g1.printcamerainfo()
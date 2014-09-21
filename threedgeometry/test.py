#!/usr/bin/env python

from camera import Camera


cam = Camera()
config_file = 'C:\Users\Borja\PycharmProjects\TFM\data\grazptz\set1\cameracalib\camera001.cfg'
cam.readconfigfile(config_file)
cam.printcamerainfo()
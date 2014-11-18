#!/usr/bin/env python

from datasets import cp
from var import variables


def selectdataset():

    while 1:
        options = \
            "\nDatasets options:\n" \
            "   1. Graz PTZ set 1\n" \
            "   2. Graz PTZ set 2\n" \
            "   3. Pets 09 citycenter 1\n" \
            "   4. Pets 09 citycenter 2\n" \
            "   5. Pets 09 regularflow 1\n" \
            "   6. Pets 09 regularflow 2\n" \
            "   7. Pets 09 regularflow 3\n" \
            "   8. Pets 09 regularflow 4\n" \
            "   9. Pets 09 regularflow 5\n" \
            "   10. Pets 09 l1 1\n" \
            "   11. Pets 09 l1 2\n"

        print options

        ans = raw_input('Please select one option: ')

        if 0 < int(ans) <= len(variables.datasets_name):
            return variables.datasets_name[int(ans)]


def saveconfiguration(cameras, configuration, bg_models):

    print '\nSaving configurations ...'

    c = cp.ConfigParser()
    c.read(configuration['dir'])

    c = saveglobalconfiguration(c, bg_models[0].bg)

    for ii in range(len(bg_models)):

        c = savebgconfiguration(c, bg_models[ii], cameras[ii].id)

    config_file = open(configuration['dir'], 'w+')
    c.write(config_file)
    config_file.close()


def saveglobalconfiguration(c, bg):

    c.set('global', 'option', bg.option)
    c.set('global', 'alpha', bg.alpha)
    c.set('global', 'beta', bg.beta)
    c.set('global', 'frame_count', bg.frame_count)
    c.set('global', 'threshold_1', bg.threshold_1)
    c.set('global', 'threshold_2', bg.threshold_2)

    return c


def savebgconfiguration(c, bg, cam):

    c.set(cam, 'win_height', bg.win_height)
    c.set(cam, 'win_width', bg.win_width)
    c.set(cam, 'win_min_pix', bg.win_min_pix)

    return c

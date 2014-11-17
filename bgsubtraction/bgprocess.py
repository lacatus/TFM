#!/usr/bin/env python

from bgsubtraction.background import Bg
from bgsubtraction.background import Background


def getbgobject(config):

    bg = Bg()
    #bg.setdefault()
    bg.setconfiguration(config)

    return bg


def getbgmodels(frames, bg, config):

    bg_models = []

    aux = 1

    for img in frames:
        bg_aux = Background(bg)
        #bg_aux.setdefault(img)
        bg_aux.setconfiguration(img, config['cam00%s' % str(aux)])

        bg_models.append(bg_aux)

        aux += 1

    return bg_models


def getbgimg(bg_models):

    bg_imgs = []

    for bg in bg_models:
        bg_imgs.append(bg.bg_img)

    return bg_imgs


def getbinimg(bg_models):

    bin_imgs = []

    for bg in bg_models:
        bin_imgs.append(bg.bin_img_1)

    return bin_imgs


def getscanimg(bg_models):

    scan_imgs = []

    for bg in bg_models:
        scan_imgs.append(bg.scan_img)

    return scan_imgs


def getdiffimg(bg_models):

    diff_imgs = []

    for bg in bg_models:
        diff_imgs.append(bg.diff_img_copy)

    return diff_imgs


def bgprocess(frames, bg_models):

    for ii in range(len(frames)):
        bg_models[ii].updatebackground(frames[ii])
        bg_models[ii].subtractbackground(frames[ii])
        bg_models[ii].windowscanbackground()
        bg_models[ii].thresholdbackground()
        bg_models[ii].contoursbackground()

    return bg_models

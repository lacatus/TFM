#!/usr/bin/env python

from bgsubtraction.background import Bg
from bgsubtraction.background import Background


def getbgobject():

    bg = Bg()
    bg.setdefault()

    return bg


def getbgmodels(frames, bg):

    bg_models = []

    for img in frames:
        bg_aux = Background(bg)
        bg_aux.setdefault(img)

        bg_models.append(bg_aux)

    return bg_models


def updatebgmodels(frames, bg_models):

    for ii in range(len(frames)):
        bg_models[ii].updatebackground(frames[ii])
        bg_models[ii].subtractbackground(frames[ii])
        bg_models[ii].windowscanbackground()
        bg_models[ii].thresholdbackground()
        bg_models[ii].contoursbackground()

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
        diff_imgs.append(bg.diff_img)

    return diff_imgs
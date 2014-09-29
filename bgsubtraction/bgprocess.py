#!/usr/bin/env python

from bgsubtraction.background import Bg
from bgsubtraction.background import Background


def getbgmodels(frames):

    bg = Bg()
    bg.setdefault()

    bg_models = []

    for img in frames:
        bg_aux = Background(bg)
        bg_aux.setdefault(img)

        bg_models.append(bg_aux)

    return bg_models


def updatebgmodels(frames, bg_models):

    for i in range(len(frames)):
        bg_models[i].updatebackground(frames[i])

    return bg_models


def getbgimg(bg_models):

    bg_imgs = []

    for bg in bg_models:
        bg_imgs.append(bg.bg_img)

    return bg_imgs


def getbinimg():  # TODO
    pass
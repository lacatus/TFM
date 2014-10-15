#!/usr/bin/env python

# Datasets imports
import datasets.datasetloader
import datasets.grazptz1
import datasets.grazptz2
import datasets.icglab1
import datasets.icglab2
import datasets.icglab3
import datasets.icglab4
import datasets.icglab5
import datasets.icglab6

# 3D geometry imports
import threedgeometry.frameretriever

# Gui imports
from gui import imshow
from gui import trackbar

# Imgproc imports
from imgproc import rgb2gray

# Background imports
from bgsubtraction import bgprocess


def initcameras():

    dataset = datasets.datasetloader.selectdataset()

    load_cmd = 'datasets.%s.loaddataset()' % dataset
    cameras = eval(load_cmd)  # execute whatever is inside the string

    cameras = threedgeometry.frameretriever.getnumcameras(cameras)

    return cameras


def initloop(cameras):

    frames = threedgeometry.frameretriever.getframes(cameras)

    bg = bgprocess.getbgobject()
    bg_models = bgprocess.getbgmodels(frames, bg)

    # Init trackbars
    trackbar.setdefaulttrackbarmain(bg)
    trackbar.setdefaulttrackbardsecondary(bg_models)

    return bg_models


def loop():

    cameras = initcameras()

    bg_models = initloop(cameras)

    while True:

        option = bg_models[0].bg.option  # get which img you want to visualize

        frames = threedgeometry.frameretriever.getframes(cameras)

        if not frames:  # Video ended
            break

        bg_models = bgprocess.updatebgmodels(frames, bg_models)

        if option is 0:
            imshow.showallimg(frames)

        elif option is 1:
            imshow.showallimg(gray_frames)

        elif option is 2:
            imshow.showallimg(bgprocess.getbgimg(bg_models))

        elif option is 3:
            imshow.showallimg(bgprocess.getbinimg(bg_models))

        elif option is 4:
            imshow.showallimg(bgprocess.getscanimg(bg_models))

        elif option is 5:
            imshow.showallimg(bgprocess.getdiffimg(bg_models))

        elif option is 6:
            imshow.showallimg(imshow.paintcontours(frames, bg_models))

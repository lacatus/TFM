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

# Imgproc imports
from imgproc import rgb2gray

# Background imports
from bgsubtraction import bgprocess


def init_loop(cameras):

    frames = threedgeometry.frameretriever.getframes(cameras)

    gray_frames = rgb2gray.rgb2graytransform(frames)

    bg_models = bgprocess.getbgmodels(gray_frames)

    return bg_models


def loop():

    dataset = datasets.datasetloader.selectdataset()

    load_cmd = 'datasets.%s.loaddataset()' % dataset
    cameras = eval(load_cmd)  # execute whatever is inside the string

    bg_models = init_loop(cameras)

    option = imshow.init_imshow()

    while True:

        frames = threedgeometry.frameretriever.getframes(cameras)

        if not frames: # Video ended
            break

        gray_frames = rgb2gray.rgb2graytransform(frames)

        bg_models = bgprocess.updatebgmodels(gray_frames, bg_models)

        if option is 1:
            imshow.showallimg(frames)

        elif option is 2:
            imshow.showallimg(gray_frames)

        elif option is 3:
            imshow.showallimg(bgprocess.getbgimg(bg_models))

        elif option is 4:
            imshow.showallimg(bgprocess.getbinimg(bg_models))

        elif option is 5:
            imshow.showallimg(bgprocess.getscanimg(bg_models))
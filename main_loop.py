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

import threedgeometry.frameretriever

# Gui imports
from gui import imshow


def loop():

    dataset = datasets.datasetloader.selectdataset()
    load_cmd = 'datasets.%s.loaddataset()' % dataset
    cams = eval(load_cmd)  # execute whatever is inside the string

    while True:

        frames = threedgeometry.frameretriever.getframes(cams)

        if not frames:
            break

        imshow.showallimg(frames)
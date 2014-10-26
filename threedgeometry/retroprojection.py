#!/usr/bin/env python

from threedgeometry import cv2

# TODO
"""
- Find contour mass center
- Find lowest contour point underneath center
- Plot point in image
- Find a way to perfectionate those selections
- Retroproject
- Diferrenciate between groups and persons
    - Use retroprojection for this cause
    - Single person --> center of mass --> lowest point underneath it is floor
    - Groups / Intersections ????
"""


def contoursmasscenter(frames, bg_models):

    for ii in range(len(frames)):

        for cont in bg_models[ii].contours:

            M = cv2.moments(cont)
            centroid_x = int(M['m10']/M['m00'])
            centroid_y = int(M['m01']/M['m00'])

            cv2.circle(
                frames[ii], (centroid_x, centroid_y),
                2, (255, 255, 0), thickness=4, lineType=8, shift=0)

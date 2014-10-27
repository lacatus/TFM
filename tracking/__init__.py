#!/usr/bin/env python

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

NEW THOUGHTS
- Maybe try to pass contours handling to this module <--- TODO ################
- Class that creates "persons" --> Blob
    - X&Y projection of contours (opencv --> core --> reduce)
        - try to plot it
    - person or group differentiation
        - person --> basic normal distribution of contours projection
        - groups --> more complex methods (papers)
- Class that manipulates all info of each "person" --> Subject
- Class that manipulates all info of each "person" situation
    - For tracking between frames
"""

import cv2

#!/usr/bin/env python

from datasets import variables


def selectdataset():

    while 1:
        options = """
            Datasets options:
                1. Graz PTZ set 1
                2. Graz PTZ set 2
                3. Icglab chap
                4. Icglab leaf 1
                5. Icglab leaf 2
                6. Icglab much
                7. Icglab pose
                8. Icglab table
            """

        print options

        ans = raw_input('Please select one option: ')

        if 0 < int(ans) <= len(variables.datasets_name):
            return variables.datasets_name[int(ans)]
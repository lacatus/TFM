#!/usr/bin/env python

from datasets import variables


def selectdataset():

    while 1:
        options = \
            "\nDatasets options:\n" \
            "   1. Graz PTZ set 1\n" \
            "   2. Graz PTZ set 2\n" \
            "   3. Icglab chap\n" \
            "   4. Icglab leaf 1\n" \
            "   5. Icglab leaf 2\n" \
            "   6. Icglab much\n" \
            "   7. Icglab pose\n" \
            "   8. Icglab table\n"

        print options

        ans = raw_input('Please select one option: ')

        if 0 < int(ans) <= len(variables.datasets_name):
            return variables.datasets_name[int(ans)]
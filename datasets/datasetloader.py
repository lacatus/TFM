#!/usr/bin/env python

from var import variables


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
            "   8. Icglab table\n" \
            "   9. Pets 09 citycenter 1\n" \
            "   10. Pets 09 citycenter 2\n" \
            "   11. Pets 09 regularflow 1\n" \
            "   12. Pets 09 regularflow 2\n" \
            "   13. Pets 09 regularflow 3\n" \
            "   14. Pets 09 regularflow 4\n" \
            "   15. Pets 09 regularflow 5\n" \
            "   16. Pets 09 l1 1\n" \
            "   17. Pets 09 l1 2\n"

        print options

        ans = raw_input('Please select one option: ')

        if 0 < int(ans) <= len(variables.datasets_name):
            return variables.datasets_name[int(ans)]

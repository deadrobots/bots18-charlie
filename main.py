#!/usr/bin/python
import os, sys
from wallaby import *
import constants as c
import motors as m
import actions as a




def main():
    a.drive_distance_test()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();









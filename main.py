#!/usr/bin/python
import os, sys
from wallaby import *
import constants as c
import motors as m
import actions as a
import utils as u
import camera as x
import gyro as g


def main():
    print("running")
    g.simple_drive_with_gyro(50, 15)


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()

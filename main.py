#!/usr/bin/python
import os, sys
from wallaby import *
import constants as c
import motors as m
import actions as a
import utils as u
import camera as x
import lego_motors as g
import create_motors as cg


def main():
    print("running")
    create_connect()
    cg.create_drive_timed(300, 3)




    create_disconnect()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()

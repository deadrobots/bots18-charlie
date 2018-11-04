#!/usr/bin/python
import os, sys
from wallaby import *
import constants as c
import motors as m
import actions as a
import utils as u
import camera as x


def main():
    a.init()
    #x.camera_test()
    #a.get_can_sensors()
    #a.get_can_camera()
    #x.camera_test()

    x.find_pom_improved(c.CHANNEL_GREEN)








if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
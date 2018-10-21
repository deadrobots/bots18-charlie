#!/usr/bin/python
import os, sys
from wallaby import *
import constants as c
import motors as m
import actions as a
import utils as u
import camera as x

# Great code overall. Some notes:
# get_soda_can() vs lineFollow() - use consistent function naming conventions.
#


def main():
    a.init()
    #x.camera_test()
    x.find_pom_improved(c.CHANNEL_RED)


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();









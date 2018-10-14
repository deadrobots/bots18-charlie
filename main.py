#!/usr/bin/python
import os, sys
from wallaby import *
import constants as c
import motors as m
import actions as a
import utils as u




def main():
    enable_servos()
    a.get_can_even_better()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();









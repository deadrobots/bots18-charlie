#!/usr/bin/python
import os, sys
from wallaby import *
import constants as c


def drive_timed(lspeed, rspeed, time):
    motor(c.LEFT_MOTOR, lspeed)
    motor(c.RIGHT_MOTOR, rspeed)
    msleep(time)
    ao()


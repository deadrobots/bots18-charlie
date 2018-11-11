#!/usr/bin/python
import motors as m
from wallaby import *
import utils as u
import constants as c
import random


def bumpy():
    print("bumping")
    while True:
        while gyro_y() > -150:
            m.drive_timed(70, 70, 1)
        print(gyro_y())
        m.drive_timed(-100, -100, 1000)
        x = random.randint(500, 1500)
        msleep(10)
        m.drive_timed(100, -100, x)


def test():
    while True:
        m.drive_timed(100, 100, 10)
        print(gyro_y())
        msleep(10)

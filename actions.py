#!/usr/bin/python
import motors as m
from wallaby import *
import utils as u
import constants as c
import random


def bumpy():
    print("bumping")
    u.move_servo(c.servo_claw, c.claw_closed, 10)
    msleep(700)
    u.move_servo(c.servo_arm, c.arm_up, 10)
    msleep(700)
    while True:
        while gyro_y() < 20:
            m.drive_timed(100, 100, 1)
        m.drive_timed(-100, -100, 1000)
        x = random.randint(500, 3000)
        m.drive_timed(100, -100, x)

def test():
    while True:
        print(gyro_y())
        m.drive_timed(100, 100, 1)

#!/usr/bin/python
import motors as m
from wallaby import *
import utils as u
import constants as c


def bumpy():
    print("bumping")
    u.move_servo(c.servo_claw, c.claw_closed, 10)
    msleep(700)
    u.move_servo(c.servo_arm, c.arm_up, 10)
    msleep(700)
    while gyro_z() < 150:
        m.drive_timed(100, 100, 1)

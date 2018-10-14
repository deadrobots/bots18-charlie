#!/usr/bin/python
import os, sys
from wallaby import *
import utils as u
import motors as m
import constants as c

def driveBox():
    print("WORKED!")
    u.wait4Button()
    m.drive_timed(100, 100, 1000)
    m.drive_timed(-100, -100, 1000)

    for i in range(0, 4):
        m.drive_timed(100, 100, 2000)
        m.drive_timed(100, 0, 1400)


def get_soda_can():
    u.wait4Button()
    u.move_servo(c.servoArm, c.armDown, 10)
    u.move_servo(c.servoClaw, c.clawOpen, 10)
    msleep(1000)
    m.drive_timed(100, 100, 1000)
    msleep(500)
    u.move_servo(c.servoClaw,c.clawClosed,10)
    u.move_servo(c.servoArm, c.armUp, 10)


def get_can_imporved(): #line follow on the straight line and grab the can
    u.move_servo(c.servoArm, c.armDown, 10)
    u.move_servo(c.servoClaw, c.clawOpen, 10)
    u.lineFollowCan(80)
    m.drive_timed(50, 50, 1000)
    msleep(500)
    u.move_servo(c.servoClaw, c.clawClosed, 10)
    u.move_servo(c.servoArm, c.armUp, 10)
    m.drive_timed(100, 0, 1400)
    u.move_servo(c.servoArm, c.armDown, 10)
    msleep(500)
    u.move_servo(c.servoClaw, c.clawOpen, 10)


def get_can_even_better(): #line follow on the curved line and grab the can
    u.move_servo(c.servoArm, c.armDown, 10)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawOpen, 10)
    u.lineFollowAmazing()
    m.drive_timed(50, 50, 1000)
    u.move_servo(c.servoClaw, c.clawClosed, 10)
    msleep(100)
    u.move_servo(c.servoArm, c.armUp, 10)


#!/usr/bin/python
import os, sys
from wallaby import *
import utils as u
import motors as m
import constants as c
import camera


def init():
    enable_servos()
    camera.camera_init()


def drive_box():
    print("WORKED!")
    u.wait_4_button()
    m.drive_timed(100, 100, 1000)
    m.drive_timed(-100, -100, 1000)

    for i in range(0, 4):
        m.drive_timed(100, 100, 2000)
        m.drive_timed(100, 0, 1400)


def get_soda_can():
    u.wait_4_button()
    u.move_servo(c.servo_arm, c.arm_down, 10)
    u.move_servo(c.servo_claw, c.claw_open, 10)
    msleep(1000)
    m.drive_timed(100, 100, 1000)
    msleep(500)
    u.move_servo(c.servo_claw, c.clawClosed, 10)
    u.move_servo(c.servo_arm, c.arm_up, 10)


def get_can_imporved(): #line follow on the straight line and grab the can
    u.move_servo(c.servo_arm, c.arm_down, 10)
    u.move_servo(c.servo_claw, c.claw_open, 10)
    u.line_follow_can(80)
    m.drive_timed(50, 50, 1000)
    msleep(500)
    u.move_servo(c.servo_claw, c.clawClosed, 10)
    u.move_servo(c.servo_arm, c.arm_up, 10)
    m.drive_timed(100, 0, 1400)
    u.move_servo(c.servo_arm, c.arm_down, 10)
    msleep(500)
    u.move_servo(c.servo_claw, c.claw_open, 10)


def get_can_even_better(): #line follow on the curved line and grab the can
    u.move_servo(c.servo_arm, c.arm_down, 10)
    msleep(100)
    u.move_servo(c.servo_claw, c.claw_open, 10)
    u.line_follow_amazing()
    m.drive_timed(50, 50, 1000)
    u.move_servo(c.servo_claw, c.clawClosed, 10)
    msleep(100)
    u.move_servo(c.servo_arm, c.arm_up, 10)


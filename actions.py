#!/usr/bin/python
import os, sys
from wallaby import *
import utils as u
import motors as m
import constants as c
import camera
import variables as v
import threading as t


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
    u.move_servo(c.servo_claw, c.claw_closed, 10)
    u.move_servo(c.servo_arm, c.arm_up, 10)


def get_can_imporved(): #line follow on the straight line and grab the can
    u.move_servo(c.servo_arm, c.arm_down, 10)
    u.move_servo(c.servo_claw, c.claw_open, 10)
    u.line_follow_can(80)
    m.drive_timed(50, 50, 1000)
    msleep(500)
    u.move_servo(c.servo_claw, c.claw_closed, 10)
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
    u.move_servo(c.servo_claw, c.claw_closed, 10)
    msleep(100)
    u.move_servo(c.servo_arm, c.arm_up, 10)


def get_can_camera(color):
    while True:
        u.move_servo(c.servo_claw, c.claw_open, 10)
        msleep(500)
        u.move_servo(c.servo_arm, c.arm_down, 10)
        msleep(500)
        camera.get_can(color)
        m.drive_timed(-50, -50, 2100)
        m.drive_timed(50, -50, 2100)
        camera_update()
        msleep(750)
        print(get_object_count(color))
        v.first_time = False


def claw():
    open = True
    start_time = seconds()
    while v.button_pressed is False:
        if seconds() - start_time > .907:
            if open:
                set_servo_position(c.servo_claw, c.claw_closed)
            else:
                set_servo_position(c.servo_claw, c.claw_open)
            open = not open
            start_time = seconds()


def drive():
    while v.button_pressed is False:
        motor(c.LEFT_MOTOR, 100)
        motor(c.RIGHT_MOTOR, 100)
    ao()


def challenge():
    go = t.Thread(name = 'daemon', target = drive)
    claw1 = t.Thread(name = 'daemon', target = claw)
    go.start()
    claw1.start()
    while left_button() == 0:
        pass
    v.button_pressed = True



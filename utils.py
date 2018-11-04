#!/usr/bin/python
import os, sys
from wallaby import *
import constants as c
import motors as m


def wait_4_button():
    print("waiting for button")
    ao()
    while right_button() == 0:
        pass
    print("pressed")


def line_follow(speed, time): #Cheet for the curved line
    while analog(c.ET) < 2000:
        sec = seconds()
        while seconds() - sec < time:
            if analog(c.top_hat) < 2600:
                m.drive_timed(speed, speed/2, 1)
            else:
                m.drive_timed(speed/2, speed, 1)
        m.drive_timed(speed/4, speed, 2800)
        while True:
            if analog(c.top_hat) < 2600:
                m.drive_timed(speed, speed/4, 1)
            else:
                m.drive_timed(speed/4, speed, 1)


def line_follow_can(speed): #works only for the straight line
    while analog(c.ET) < 2000:
        if analog(c.top_hat) < 3000:
            m.drive_timed(speed, speed/2, 1)
        else:
            m.drive_timed(speed/2, speed, 1)

def line_follow_ugly(speed): #looks bad but works for all lines
    while analog(c.ET) < 2000:
        if analog(c.top_hat) < 2500:
            motor(c.LEFT_MOTOR, speed)
            motor(c.RIGHT_MOTOR, 0)
        else:
            motor(c.RIGHT_MOTOR, speed)
            motor(c.LEFT_MOTOR, 0)

# Nice idea. Here's a thought for you (don't necessarily program this)
# Can you re-write this function so that instead of an if/else cascade, you have a mathematical 
# function to adjust the motor's speed using an equation? - LMB
def line_follow_amazing(): #make sure this works for a straight line and the curved line
    while analog(c.ET) < 2000:
        if analog(c.top_hat) < 400:
            motor(c.LEFT_MOTOR, 100)
            motor(c.RIGHT_MOTOR, 15)
        elif analog(c.top_hat) < 600:
            motor(c.LEFT_MOTOR, 80)
            motor(c.RIGHT_MOTOR, 60)
        elif analog(c.top_hat) < 800:
            motor(c.LEFT_MOTOR, 80)
            motor(c.RIGHT_MOTOR, 80)
        elif analog(c.top_hat) < 1100:
            motor(c.LEFT_MOTOR, 60)
            motor(c.RIGHT_MOTOR, 80)
        else:
            motor(c.LEFT_MOTOR, 15)
            motor(c.RIGHT_MOTOR, 100)


def move_servo(servo_port, end_position, speed):  # controls speed of servo movement
    print ("moving servo")
    pos = get_servo_position(servo_port)
    i = speed
    while end_position != pos and abs(i) + abs(pos) < end_position:
        if pos < end_position:
            set_servo_position(servo_port, pos)
            msleep(10)
            pos = pos + i
        else:
            set_servo_position(servo_port, pos)
            msleep(10)
            pos = pos - i
    set_servo_position(servo_port, end_position)


def find_edge():
    m.drive_timed(-50, 50, 3000)
    while digital(c.button) != 1:
        m.drive_timed(50, 50, 1)
    move_servo(c.servo_arm, c.arm_up, 10)
    msleep(500)
    m.drive_timed(20, 20, 1300)
    move_servo(c.servo_claw, c.claw_open, 10)








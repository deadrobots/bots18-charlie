#!/usr/bin/python
import os, sys
from wallaby import *
import constants as c
import motors as m

def wait4Button():
    print("waiting for button")
    ao()
    while right_button() == 0:
        pass
    print("pressed")


def move_servo(servoPort, endPosition, speed):
    enable_servos()
    print ("moving servo")
    pos = get_servo_position(servoPort)
    if (endPosition > pos ):
        i = speed
        while (pos < endPosition):
            set_servo_position(servoPort, pos)
            msleep(10)
            pos = pos + i
    elif (endPosition < pos):
        i = speed
        while (pos > endPosition):
            set_servo_position(servoPort, pos)
            msleep(10)
            pos = pos - i
    set_servo_position(servoPort, endPosition)


def lineFollow(speed):
    while True:
        if analog(c.topHat) < 3000:
            m.drive_timed(speed, speed/2, 1)
        else:
            m.drive_timed(speed/2, speed, 1)


def lineFollowCan(speed):
    while analog(c.ET) < 2000:
        if analog(c.topHat) < 3000:
            m.drive_timed(speed, speed/2, 1)
        else:
            m.drive_timed(speed/2, speed, 1)



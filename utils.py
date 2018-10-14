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


def move_servo(servoPort, endPosition, speed): #controls speed of servo movement
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


def lineFollow(speed, time): #timed line follow for straight line
    while analog(c.ET) < 2000:
        sec = seconds()
        while seconds() - sec < time:
            if analog(c.topHat) < 2600:
                m.drive_timed(speed, speed/2, 1)
            else:
                m.drive_timed(speed/2, speed, 1)
        m.drive_timed(speed/4, speed, 2800)
        while True:
            if analog(c.topHat) < 2600:
                m.drive_timed(speed, speed/4, 1)
            else:
                m.drive_timed(speed/4, speed, 1)


def lineFollowCan(speed): #works only for the straight line
    while analog(c.ET) < 2000:
        if analog(c.topHat) < 3000:
            m.drive_timed(speed, speed/2, 1)
        else:
            m.drive_timed(speed/2, speed, 1)

def lineFollowUgly(speed): #looks bad but works for all lines
    while analog(c.ET) < 2000:
        if analog(c.topHat) < 2500:
            motor(c.LEFT_MOTOR, speed)
            motor(c.RIGHT_MOTOR, 0)
        else:
            motor(c.RIGHT_MOTOR, speed)
            motor(c.LEFT_MOTOR, 0)


def lineFollowAmazing(): #make sure this works for a straight line and the curved line
    while analog(c.ET) < 2000:
        if analog(c.topHat) < 400:
            motor(c.LEFT_MOTOR, 100)
            motor(c.RIGHT_MOTOR, 15)
        elif analog(c.topHat) < 600:
            motor(c.LEFT_MOTOR, 80)
            motor(c.RIGHT_MOTOR, 60)
        elif analog(c.topHat) < 800:
            motor(c.LEFT_MOTOR, 80)
            motor(c.RIGHT_MOTOR, 80)
        elif analog(c.topHat) < 1100:
            motor(c.LEFT_MOTOR, 60)
            motor(c.RIGHT_MOTOR, 80)
        else:
            motor(c.LEFT_MOTOR, 15)
            motor(c.RIGHT_MOTOR, 100)


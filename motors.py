#!/usr/bin/python
import os, sys
from wallaby import *
import constants as c

def drive_timed(lspeed, rspeed, time):
    motor(c.LEFT_MOTOR, lspeed)
    motor(c.RIGHT_MOTOR, rspeed)
    msleep(time)
    ao()

def drive_distance(speed, distance):
    clear_motor_position_counter(c.LEFT_MOTOR)
    if speed > 0:
        while get_motor_position_counter(c.LEFT_MOTOR) < distance * 200:
            drive_timed(speed, speed, 1)
    elif speed < 0:
        while get_motor_position_counter(c.LEFT_MOTOR) > distance * 200:
            drive_timed(speed, speed, 1)
    ao()
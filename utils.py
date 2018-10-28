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

# # This method can probably be re-written to be just a single WHILE statement, with one IF/ELSE statement inside. -LMB
# def move_servo(servoPort, endPosition, speed): #controls speed of servo movement
#     enable_servos() # This should be handled in your main() function - LMB
#     print ("moving servo")
#     pos = get_servo_position(servoPort)
#     if endPosition > pos: # Unnecessary parentheses here. Also incorrect in my software documentation (sry), but please fix - LMB
#         i = speed
#         while pos < endPosition: # Technically unnecessary parentheses here - LMB
#             set_servo_position(servoPort, pos)
#             msleep(10)
#             pos = pos + i
#     elif endPosition < pos:
#         i = speed
#         while pos > endPosition:
#             set_servo_position(servoPort, pos)
#             msleep(10)
#             pos = pos - i
#     set_servo_position(servoPort, endPosition)


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


def move_servo(servoPort, endPosition, speed): #controls speed of servo movement
    print ("moving servo")
    pos = get_servo_position(servoPort)
    i = speed
    while endPosition != pos and abs(i) + abs(pos) < endPosition:
        # if abs(i) + abs(pos) > endPosition:
        #     set_servo_position(servoPort, pos)
        #     break
        if pos < endPosition:
            set_servo_position(servoPort, pos)
            msleep(10)
            pos = pos + i
        else:
            set_servo_position(servoPort, pos)
            msleep(10)
            pos = pos - i
    set_servo_position(servoPort, endPosition)





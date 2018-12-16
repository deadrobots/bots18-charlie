#!/usr/bin/python
from wallaby import *
import constants as c
import math
import variables as v
import threading
import utils as u


INCHES_TO_TICKS = 319

"""
BTW I got my code reviews all done before mednight this time! ;)

Great code overall. New challenge for you, if you're up for it.

You can use threads. That's great. Now this: Using threads, make your robot drive forward (straight)
using the gyro, also while moving its arm up and down, and in another thread, make the robot
open and close its claw. I want the claw to change direction (open/close) every 907 milliseconds (exactly) and I want the arm to change direction every 2467 milliseconds (exactly). I also want the
robot to drive straight. I want it to do this forever.

THEN, I want all motion (arms, claws, and motors) to IMMEDIATELY cease when the left button is
pressed. Just pressed, not pressed-and-held-down. I only want to see you checking the button (via
analog() or the left-button-funciton() once in your code... in a loop of course, but yeah)

I think you can figure this one out. Have fun! -LMB
"""
def drive_and_servo():
    drive = threading.Thread(name = 'deamon', target = lambda: drive_distance(100,100))
    drive.start()
    while True:
        u.move_servo(c.servo_arm, c.arm_down, 10)
        msleep(500)
        u.move_servo(c.servo_arm, c.arm_up, 10)
        msleep(500)


def _clear_ticks():
    clear_motor_position_counter(c.RIGHT_MOTOR)
    clear_motor_position_counter(c.LEFT_MOTOR)


def _freeze_motors():
    freeze(c.LEFT_MOTOR)
    freeze(c.RIGHT_MOTOR)


def _calibrate_gyro():
    i = 0
    avg = 0
    while i < 50:
        avg = avg + gyro_z()
        msleep(1)
        i = i + 1
    v.bias = avg/50


def drive_timed(speed, time):
    print("Driving for time")
    _calibrate_gyro()
    start_time = seconds()
    theta = 0
    while seconds() - start_time < time:
        if speed > 0:
            motor(c.RIGHT_MOTOR, int((speed - speed * (1.920137e-16 + 0.000004470956*theta))))
            motor(c.LEFT_MOTOR, int((speed + speed * (1.920137e-16 + 0.000004470956*theta))))
        else:
             motor(c.RIGHT_MOTOR, int((speed + speed * (1.920137e-16 + 0.000004470956*theta))))
             motor(c.LEFT_MOTOR, int((speed - speed * (1.920137e-16 + 0.000004470956*theta))))
        msleep(10)
        theta = theta + (gyro_z() - v.bias) * 10
    _freeze_motors()

                                                  # All of these turn/pivots using the gyro to make the turn or pivot excact
def turn_with_gyro(left_wheel_speed, right_wheel_speed, target_theta_deg):
    _calibrate_gyro()
    print("turning")
    target_theta = round(target_theta_deg * v.turn_conversion)
    theta = 0
    while theta < target_theta:
        motor(c.RIGHT_MOTOR, right_wheel_speed)
        motor(c.LEFT_MOTOR, left_wheel_speed)
        msleep(10)
        theta = theta + abs(gyro_z() - v.bias) * 10
    print(theta)
    _freeze_motors()


def pivot_on_left_wheel(right_wheel_speed, target_theta_deg):
    _calibrate_gyro()
    print("pivoting on left")
    target_theta = round(target_theta_deg * v.turn_conversion)
    theta = 0
    while theta < target_theta:
        motor(c.RIGHT_MOTOR, right_wheel_speed)
        motor(c.LEFT_MOTOR, 0)
        msleep(10)
        theta = theta + abs(gyro_z() - v.bias) * 10
    motor(c.LEFT_MOTOR, 0)
    motor(c.RIGHT_MOTOR, 0)
    _freeze_motors()


def pivot_on_right_wheel(left_wheel_speed, target_theta_deg):
    _calibrate_gyro()
    print("pivoting on right")
    target_theta = round(target_theta_deg * v.turn_conversion)
    theta = 0
    while theta < target_theta:
        motor(c.RIGHT_MOTOR, 0)
        motor(c.LEFT_MOTOR, left_wheel_speed)
        msleep(10)
        theta = theta + abs(gyro_z() - v.bias) * 10
    motor(c.LEFT_MOTOR, 0)
    motor(c.RIGHT_MOTOR, 0)
    _freeze_motors()


def drive_distance(speed, distance):
    _calibrate_gyro()
    _clear_ticks()
    print("Driving for distance")
    theta = 0
    while abs((get_motor_position_counter(c.RIGHT_MOTOR) + get_motor_position_counter(c.LEFT_MOTOR)/2)) < distance * INCHES_TO_TICKS:
        if speed > 0:
            motor(c.RIGHT_MOTOR, int((speed - speed * (1.920137e-16 + 0.000004470956*theta))))
            motor(c.LEFT_MOTOR, int((speed + speed * (1.920137e-16 + 0.000004470956*theta))))
        else:
             motor(c.RIGHT_MOTOR, int((speed + speed * (1.920137e-16 + 0.000004470956*theta))))
             motor(c.LEFT_MOTOR, int((speed - speed * (1.920137e-16 + 0.000004470956*theta))))
        msleep(10)
        theta = theta + (gyro_z() - v.bias) * 10
    _freeze_motors()


def drive_condition(speed, test_function, state = True): #Needs some work
    print("Driving while condition is inputted state")
    _calibrate_gyro()
    theta = 0
    while test_function() is state:
        if speed > 0:
            motor(c.RIGHT_MOTOR, int((speed - speed * (1.920137e-16 + 0.000004470956 * theta))))
            motor(c.LEFT_MOTOR, int((speed + speed * (1.920137e-16 + 0.000004470956 * theta))))
        else:
            motor(c.RIGHT_MOTOR, int((speed + speed * (1.920137e-16 + 0.000004470956 * theta))))
            motor(c.LEFT_MOTOR, int((speed - speed * (1.920137e-16 + 0.000004470956 * theta))))
        msleep(10)
        theta = theta + (gyro_z() - v.bias) * 10
    _freeze_motors()


def _drive(speed):
    print("Driving for time")
    _calibrate_gyro()
    theta = 0
    while True:
        if speed > 0:
            motor(c.RIGHT_MOTOR, int((speed - speed * (1.920137e-16 + 0.000004470956*theta))))
            motor(c.LEFT_MOTOR, int((speed + speed * (1.920137e-16 + 0.000004470956*theta))))
        else:
             motor(c.RIGHT_MOTOR, int((speed + speed * (1.920137e-16 + 0.000004470956*theta))))
             motor(c.LEFT_MOTOR, int((speed - speed * (1.920137e-16 + 0.000004470956*theta))))
        msleep(10)
        theta = theta + (gyro_z() - v.bias) * 10
    _freeze_motors()



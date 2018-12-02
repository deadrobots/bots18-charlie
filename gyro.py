#!/usr/bin/python
from wallaby import *
import constants as c
import math
import variables as v
import threading
import utils as u


INCHES_TO_TICKS = 319


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


def simple_drive_timed(speed, time): # Way to drive using the gyro to straighten robot out
    print("Driving for time")
    print("You should probably use drive_timed instead")
    _calibrate_gyro()
    start_time = seconds()
    theta = 0
    while seconds() - start_time < time:
        if theta < 2500 and theta > -2500:
            motor(c.RIGHT_MOTOR, speed)
            motor(c.LEFT_MOTOR, speed)
        elif theta < -2500 and theta > -10000:
            motor(c.RIGHT_MOTOR, speed + 3)
            motor(c.LEFT_MOTOR, speed - 3)
        elif theta > 2500 and theta < 10000:
            motor(c.RIGHT_MOTOR, speed - 3)
            motor(c.LEFT_MOTOR, speed + 3)
        elif theta > 10000:
            motor(c.RIGHT_MOTOR, speed - 20)
            motor(c.LEFT_MOTOR, speed + 20)
        else:
            motor(c.RIGHT_MOTOR, speed + 20)
            motor(c.LEFT_MOTOR, speed - 20)
        print(theta)
        msleep(10)
        theta = theta + (gyro_z() - v.bias) * 10
    _freeze_motors()


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
    print("pivoting")
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
    print("pivoting")
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
    print("Driving straight")
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



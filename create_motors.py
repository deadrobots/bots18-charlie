#!/usr/bin/python
from wallaby import *
import variables as v
import constants as c


def _calibrate_gyro():
    i = 0
    avg = 0
    while i < 50:
        avg = avg + gyro_z()
        msleep(1)
        i = i + 1
    v.bias = avg/50


def create_drive_timed(speed, time):
    print("Driving for time")
    _calibrate_gyro()
    start_time = seconds()
    speed = -speed
    theta = 0
    while seconds() - start_time < time:
        if speed > 0:
            create_drive_direct(int((speed + speed * (1.920137e-16 + 0.000004470956 * theta))), int((speed - speed * (1.920137e-16 + 0.000004470956 * theta))))
        else:
            create_drive_direct(int((speed - speed * (1.920137e-16 + 0.000004470956 * theta))), int((speed + speed * (1.920137e-16 + 0.000004470956 * theta))))
        msleep(10)
        theta = theta + (gyro_z() - v.bias) * 10
    create_drive_direct(0, 0)


def create_turn_with_gyro(left_wheel_speed, right_wheel_speed, target_theta_deg):
    _calibrate_gyro()
    print("turning")
    target_theta = round(target_theta_deg * v.turn_conversion)
    theta = 0
    while theta < target_theta:
        create_drive_direct(-right_wheel_speed, -left_wheel_speed)
        msleep(10)
        theta = theta + abs(gyro_z() - v.bias) * 10
    print(theta)
    create_drive_direct(0, 0)


def create_pivot_on_left_wheel(left_speed, degrees):
    _calibrate_gyro()
    print("Pivoting on left wheel")
    left_speed = -left_speed
    target_theta = round(degrees * v.turn_conversion)
    theta = 0
    while theta < target_theta:
        create_drive_direct(0, left_speed)
        msleep(10)
        theta = theta + abs(gyro_z() - v.bias) * 10
    print (theta)
    create_drive_direct(0, 0)


def create_pivot_on_right_wheel(right_speed, degrees):
    _calibrate_gyro()
    print("Pivoting on left wheel")
    right_speed = -right_speed
    target_theta = round(degrees * v.turn_conversion)
    theta = 0
    while theta < target_theta:
        create_drive_direct(right_speed, 0)
        msleep(10)
        theta = theta + abs(gyro_z() - v.bias) * 10
    print (theta)
    create_drive_direct(0, 0)


def _drive(speed):
    print("Driving for time")
    _calibrate_gyro()
    speed = -speed
    theta = 0
    while True:
        if speed > 0:
            create_drive_direct(int((speed + speed * (1.920137e-16 + 0.000004470956 * theta))), int((speed - speed * (1.920137e-16 + 0.000004470956 * theta))))
        else:
            create_drive_direct(int((speed - speed * (1.920137e-16 + 0.000004470956 * theta))), int((speed + speed * (1.920137e-16 + 0.000004470956 * theta))))
        msleep(10)
        theta = theta + (gyro_z() - v.bias) * 10
    create_drive_direct(0, 0)
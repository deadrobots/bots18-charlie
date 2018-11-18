#!/usr/bin/python
from wallaby import *
import constants as c
import math
import variables as v


def calibrate_gyro():
    i = 0
    avg = 0
    while i < 50:
        avg = avg + gyro_z()
        msleep(1)
        i = i + 1
    v.bias = avg/50


def simple_drive_with_gyro(speed, time): # Way to drive using the gyro to straighten robot out
    calibrate_gyro()
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


def drive_with_gyro(speed, time): # Much more complicated and questionable way to do simple_drive_with_gyro
    calibrate_gyro()
    start_time = seconds()
    theta = 0
    while seconds() - start_time < time:
        if speed > 0:
            motor(c.RIGHT_MOTOR, int((speed - speed * (1.920137e-16 + 0.000004470956*theta - 7.399285e-28*math.pow(theta, 2) - 2.054177e-18*math.pow(theta, 3) + 1.3145e-40*math.pow(theta, 4)))))
            motor(c.LEFT_MOTOR, int((speed + speed * (1.920137e-16 + 0.000004470956*theta - 7.399285e-28*math.pow(theta, 2) - 2.054177e-18*math.pow(theta, 3) + 1.3145e-40*math.pow(theta, 4)))))
        else:
             motor(c.RIGHT_MOTOR, int((speed + speed * (1.920137e-16 + 0.000004470956*theta - 7.399285e-28*math.pow(theta, 2) - 2.054177e-18*math.pow(theta, 3) + 1.3145e-40*math.pow(theta, 4)))))
             motor(c.LEFT_MOTOR, int((speed - speed * (1.920137e-16 + 0.000004470956*theta - 7.399285e-28*math.pow(theta, 2) - 2.054177e-18*math.pow(theta, 3) + 1.3145e-40*math.pow(theta, 4)))))
        msleep(10)
        theta = theta + (gyro_z() - v.bias) * 10


                                                  # All of these turn/ pivot using the gyro to make the turn or pivot excact
def turn_with_gyro(left_wheel_speed, right_wheel_speed, target_theta_deg):
    calibrate_gyro()
    print("turning")
    target_theta = round(target_theta_deg * 5600)
    theta = 0
    while theta < target_theta:
        motor(c.RIGHT_MOTOR, right_wheel_speed)
        motor(c.LEFT_MOTOR, left_wheel_speed)
        msleep(10)
        theta = theta + abs(gyro_z() - v.bias) * 10
    print(theta)
    motor(c.LEFT_MOTOR, 0)
    motor(c.RIGHT_MOTOR, 0)


def pivot_on_left_wheel(right_wheel_speed, target_theta_deg):
    calibrate_gyro()
    print("pivoting")
    target_theta = round(target_theta_deg * 5600)
    theta = 0
    while theta < target_theta:
        motor(c.RIGHT_MOTOR, right_wheel_speed)
        motor(c.LEFT_MOTOR, 0)
        msleep(10)
        theta = theta + abs(gyro_z() - v.bias) * 10
    motor(c.LEFT_MOTOR, 0)
    motor(c.RIGHT_MOTOR, 0)


def pivot_on_right_wheel(left_wheel_speed, target_theta_deg):
    calibrate_gyro()
    print("pivoting")
    target_theta = round(target_theta_deg * 5600)
    theta = 0
    while theta < target_theta:
        motor(c.RIGHT_MOTOR, 0)
        motor(c.LEFT_MOTOR, left_wheel_speed)
        msleep(10)
        theta = theta + abs(gyro_z() - v.bias) * 10
    motor(c.LEFT_MOTOR, 0)
    motor(c.RIGHT_MOTOR, 0)







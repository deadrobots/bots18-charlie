#!/usr/bin/python
from wallaby import *
import constants as c
import motors as m
import utils as u


def camera_init():
    camera_open_black()


def camera_test():
    camera_areas = []
    while True:
        camera_update()
        camera_areas.append(get_object_area(c.CHANNEL_RED, 0))
        area_average = sum(camera_areas) / len(camera_areas)
        print(area_average)


def camera_update_wrks():
    sec = seconds()
    while seconds() - sec < 3:
        camera_update()
        msleep(250)


def find_pom(color):
    camera_update_wrks()
    camera_center = get_camera_width()/2
    while True:
        camera_update()
        if get_object_count(color) > 0:
            if camera_center == get_object_center_x(color, 0):
                print("I see something")
                print(get_object_center_x(color, 0))
                motor(c.LEFT_MOTOR, 40)
                motor(c.RIGHT_MOTOR, 40)
            elif camera_center > get_object_center_x(color, 0):
                print("I see something")
                print(get_object_center_x(color, 0))
                motor(c.LEFT_MOTOR, 20)
                motor(c.RIGHT_MOTOR, 40)
            elif camera_center < get_object_center_x(color, 0):
                print("I see something")
                print(get_object_center_x(color, 0))
                motor(c.LEFT_MOTOR, 40)
                motor(c.RIGHT_MOTOR, 20)
        else:
            m.drive_timed(-10, 10, 1)


def find_pom_improved(color): #Needs testing
    print("Searching for poms")
    camera_update_wrks()
    camera_center = get_camera_width()/2
    while True:
        camera_update()
        if get_object_count(color) > 0:
            if get_object_center_x(color, 0) < 40:  # x<40
                motor(c.LEFT_MOTOR, 0)
                motor(c.RIGHT_MOTOR, 40)
            elif get_object_center_x(color, 0) > 120:  # x>120
                motor(c.LEFT_MOTOR, 40)
                motor(c.RIGHT_MOTOR, 0)
            elif get_object_center_x(color, 0) > 40 and get_object_center_x(color, 0) < 70:  # 40<x<70
                motor(c.LEFT_MOTOR, 20)
                motor(c.RIGHT_MOTOR, 40)
            elif get_object_center_x(color, 0) > 90 and get_object_center_x(color, 0) < 120:  # 90<x<120
                motor(c.LEFT_MOTOR, 40)
                motor(c.RIGHT_MOTOR, 20)
            else:                               # 70<x<90
                motor(c.LEFT_MOTOR, 40)
                motor(c.RIGHT_MOTOR, 40)
        # else:
        #     m.drive_timed(-10, 10, 1)



def find_pom_best(color): #Needs testing
    print("Searching for poms")
    camera_update()
    camera_center = get_camera_width()/2
    while True:
        camera_update()
        if get_object_count(color) > 0 and get_object_area(color, 0) > 1300:
            if get_object_center_x(color, 0) < 40:
                motor(c.LEFT_MOTOR, 0)
                motor(c.RIGHT_MOTOR, 40)
            elif get_object_center_x(color, 0) > 120:
                motor(c.LEFT_MOTOR, 40)
                motor(c.RIGHT_MOTOR, 0)
            elif get_object_center_x(color, 0) > 40 and get_object_center_x(color, 0) < 70:
                motor(c.LEFT_MOTOR, 20)
                motor(c.RIGHT_MOTOR, 40)
            elif get_object_center_x(color, 0) > 90 and get_object_center_x(color, 0) < 120:
                motor(c.LEFT_MOTOR, 40)
                motor(c.RIGHT_MOTOR, 20)
            else:
                motor(c.LEFT_MOTOR, 40)
                motor(c.RIGHT_MOTOR, 40)
        else:
            if get_object_count(color) == 0 or get_object_area(color, 0) <= 1300:
                m.drive_timed(-10, 10, 1)
            elif get_object_count(color) > 0:# and get_object_area(color, 0) > 500:
                if get_object_center_x(color, 0) < 40:
                    motor(c.LEFT_MOTOR, 0)
                    motor(c.RIGHT_MOTOR, 40)
                elif get_object_center_x(color, 0) > 120:
                    motor(c.LEFT_MOTOR, 40)
                    motor(c.RIGHT_MOTOR, 0)
                elif get_object_center_x(color, 0) > 40 and get_object_center_x(color, 0) < 70:
                    motor(c.LEFT_MOTOR, 20)
                    motor(c.RIGHT_MOTOR, 40)
                elif get_object_center_x(color, 0) > 90 and get_object_center_x(color, 0) < 120:
                    motor(c.LEFT_MOTOR, 40)
                    motor(c.RIGHT_MOTOR, 20)
                else:
                    motor(c.LEFT_MOTOR, 40)
                    motor(c.RIGHT_MOTOR, 40)


def get_can(color):  # Works pretty well but could be better
    print("Searching for cans")
    camera_update()
    msleep(100)
    camera_areas = [0, 0, 0, 0, 0]
    area_average = get_object_area(color, 0)
    print(get_object_count(color))
    while area_average < 1400 or c.first_time is False:
        c.first_time = True
        print("Found a can")
        camera_update()
        if len(camera_areas) == 5:
            camera_areas.pop(0)
        camera_areas.append(get_object_area(color, 0))
        area_average = sum(camera_areas) / len(camera_areas)
        if get_object_count(c.CHANNEL_RED) > 0:
            if get_object_center_x(color, 0) < 40:
                motor(c.LEFT_MOTOR, 0)
                motor(c.RIGHT_MOTOR, 40)
            elif get_object_center_x(color, 0) > 120:
                motor(c.LEFT_MOTOR, 40)
                motor(c.RIGHT_MOTOR, 0)
            elif get_object_center_x(color, 0) > 40 and get_object_center_x(color, 0) < 70:
                motor(c.LEFT_MOTOR, 20)
                motor(c.RIGHT_MOTOR, 40)
            elif get_object_center_x(color, 0) > 90 and get_object_center_x(color, 0) < 120:
                motor(c.LEFT_MOTOR, 40)
                motor(c.RIGHT_MOTOR, 20)
            else:
                motor(c.LEFT_MOTOR, 40)
                motor(c.RIGHT_MOTOR, 40)
        else:
            m.drive_timed(20, -20, 1)
    print(area_average)
    m.drive_timed(48, 50, 2800)
    msleep(500)
    u.move_servo(c.servo_claw, c.claw_closed, 10)
    msleep(500)
    u.move_servo(c.servo_arm, c.arm_up, 10)
    msleep(500)
    m.drive_timed(-50, 50, 2100)
    while gyro_y() > -150:
        m.drive_timed(70, 70, 1)
    u.move_servo(c.servo_arm, c.arm_up, 10)
    msleep(500)
    u.move_servo(c.servo_claw, c.claw_open, 10)
    msleep(500)

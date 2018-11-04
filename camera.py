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
        if len(camera_areas) == 5:
            camera_areas.pop(0)
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
            camera_update() # This needs to only be run once per loop. It is unnecessary here. Remove this one <-- LMB
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



# I like the two more "gradual" cases you programmed.
# You probably knew this already, but I like how the test for 40 < x < 70 will run first and
# exit the if statement, while the next check for 90 < x < 120 would've also been "triggered",
# but since you have the more specific/smaller width first, your robot executes that code instead -LMB
def find_pom_improved(color): #Needs testing
    print("Searching for poms")
    camera_update_wrks()
    camera_center = get_camera_width()/2
    while True:
        camera_update()
        if get_object_count(color) > 0:
            camera_update() # Only  needs to be called once per loop. Remove this one <-- LMB
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
            m.drive_timed(-10, 10, 1)



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


def get_can(color): #Does not work yet :(
    print("Searching for cans")
    camera_update()
    camera_center = get_camera_width()/2
    camera_areas = []
    while True:
        camera_update()
        if len(camera_areas) == 5:
            camera_areas.pop(0)
        camera_areas.append(get_object_area(color, 0))
        area_average = sum(camera_areas) / len(camera_areas)
        if get_object_count(c.CHANNEL_RED) > 0 and area_average < 1600:
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
        elif get_object_count(c.CHANNEL_RED) > 0 and area_average >= 1600:
            m.drive_timed(25, 25, 1000)
            print(area_average)
            break	# (Is this for debugging?) dunno if you want this. "break" will hop out of your while loop 
					# If you still find that you need logic like this, then there's probably a 
					# way to re-write the While loop -LMB
        # else:
        #     m.drive_timed(-10, 10, 1)

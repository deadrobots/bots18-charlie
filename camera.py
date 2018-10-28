#!/usr/bin/python
from wallaby import *
import constants as c
import motors as m
import utils as u


def camera_init():
    camera_open_black()


def camera_test():
    camera_update_wrks()
    print(get_object_count(c.CHANNEL_RED))
    msleep(250)
    # while True:
    #     camera_update()
    #     if get_object_count(c.CHANNEL_BLUE) >= 1:
    #         print("See blue")
    #     elif get_object_count(c.CHANNEL_GREEN) >= 1:
    #         print("See green")
    #     elif get_object_count(c.CHANNEL_RED) >= 1:
    #         print("See red")


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
            camera_update() # This needs to only be run once per loop. It is unnecessary here.
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
                print("I can not see anything") 
				# May I submit to you that this line^ never runs... (probably)...
				# because you've already checked (via get_object_count()) that you are indeed seeing SOMETHING. 
				# You need to add another case to your get_object_count() check. What will your robot do if it really
				# doesn't see any objects of the color you're looking for? - LMB

def find_pom_improved(color): #Needs testing
    camera_update_wrks()
    camera_center = get_camera_width()/2
    while True:
        camera_update()
        if get_object_count(color) > 0:
            camera_update() # Only  needs to be called once per loop
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
		# Again, you probably need another case here. How does your robot search for more poms?
		# see above comments on your similar function
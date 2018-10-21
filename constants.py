#!/usr/bin/python
import os, sys
from wallaby import *

#motor ports
LEFT_MOTOR = 0
RIGHT_MOTOR = 3

#servo ports
servo_arm = 3
servo_claw = 2

#arm values
arm_down = 1070
arm_up = 550

#claw values
claw_open = 1889
clawClosed = 900

#sensor parts
top_hat = 0
ET = 5

#camera constants
CHANNEL_BLUE = 0
CHANNEL_RED = 1
CHANNEL_GREEN = 2
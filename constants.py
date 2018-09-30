#!/usr/bin/python
import os, sys
from wallaby import *

#motor ports
LEFT_MOTOR = 0
RIGHT_MOTOR = 3

#servo ports
servoArm = 3
servoClaw = 2

#arm values
armDown = 1070
armUp = 550

#claw values
clawOpen = 1889
clawClosed = 900

#sensor parts
topHat = 0
ET = 5
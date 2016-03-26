#!/usr/bin/env python
#title           : rpi_shutdown.py
#description     : Simple script for shutting down the raspberry Pi at the press of a button.
#author          : J.Pudlo (spideyk21)
#date            : 03/26/2016
#version         : 0.1
#				 : 0.2 - Added REVISON check (GPI.RPI_REVISION)

#usage           : Add to rc.local to run at boot.
#notes           :
#python_version  : 2.7
#==============================================================================

# based on script by Alex Eames http://RasPi.tv/  
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio  

import RPi.GPIO as GPIO
import time
import os


# Set Input/Outputs
GPIO.setmode(GPIO.BCM)

# Check Board Revision
	# 0 = Compute Module
	# 1 = Rev 1
	# 2 = Rev 2
	# 3 = Model B+/A+
	# ? = Model B2
if GPIO.RPI_REVISION == 1 or GPIO.RPI_REVISION == 2:
	switch_pin = 7
elif GPIO.RPI_REVISION == 3:
	switch_pin = 21
  
# GPIO (switch_pin) set up as input. It is pulled up to stop false signals  
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

try:  
  GPIO.wait_for_edge(switch_pin, GPIO.FALLING)
  time.sleep(5) # wait 5 seconds
  os.system("sudo powerdown")

except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  
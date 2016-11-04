#!/usr/bin/env python3
#title           : rpi_shutdown.py
#description     : Simple script for shutting down the raspberry Pi at the press/hold of a button.
#author          : J.Pudlo (spideyk21)
#date            : 11/04/2016
#version         : 0.1
#
#usage           : add to crontab, i.e. @reboot /[location]/rpi_shutdown.py
#
#python_version  : 3.0
#notes			 : uses gpiozero (https://gpiozero.readthedocs.org/)
#
#==============================================================================

from gpiozero import Button
import time import sleep
import os

button_pwr = Button(21)
time_delay = 2 #how long to hold power button before shutdown occures - in seconds
	
while true:
button_pwr.wait_for_press()
	time.sleep(time_delay)
	if button_pwr.is_pressed #press and hold so you dont shutdown on accidental button press
		print ("shutting down") #temp
		#os.system("sudo powerdown")
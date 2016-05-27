#!/usr/bin/env python
#title           : rpi_shutdown.py
#description     : Simple script for shutting down the raspberry Pi at the press of a button.
#author          : J.Pudlo (spideyk21)
#date            : 03/26/2016
#version         : 0.1
#
#usage           : add to crontab, i.e. @reboot /[location]/rpi_shutdown.py
#
#python_version  : 3.0
#notes			 : uses gpiozero (https://gpiozero.readthedocs.org/)
# based on script by Alex Eames http://RasPi.tv/  
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio  
#
#==============================================================================

import RPi.GPIO as GPIO
from gpiozero import Button
import time import sleep
import os

# Check Board Revision
	#http://elinux.org/RPi_HardwareHistory
	# 0 = Compute Module
	# 1 = Rev 1
	# 2 = Rev 2
	# 3 = Model B+/A+
	# 4-9 & d-f = Model B2
	# 4-9 & d-f = Pi2 Model B
	# ? = Pi Zero
	# ? = Pi3
		
gpio_header_rev = GPIO.RPI_INFO['P1_Revision']

if gpio_header_rev == 1 or gpio_header_rev == 2:
	switch_pin = 7
elif switch_pin = 21

button = Button(switch_pin) #set gpio number based on board rev.
	
while true:
button.wait_for_press()
	time.sleep(5) # wait 5 seconds
	if button.is_pressed #press and hold so you dont shutdown on accidental button press
		#os.system("sudo powerdown")
		print ("shutting down") #temp
		print ("board rev: " + gpio_header_rev + ", gpio pin: " + switch_pin) #temp
		
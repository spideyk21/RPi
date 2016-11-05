#!/usr/bin/env python3
#title           : rpi_shutdown.py
#description     : Simple script for shutting down the raspberry Pi at the press/hold of a button.
#author          : J.Pudlo (spideyk21)
#date            : 11/04/2016
#version         : 0.1
#
#usage           : add to crontab, i.e. @reboot /[location]/rpi_shutdown2.py
#
#python_version  : 3.0
#notes		 : uses gpiozero (https://gpiozero.readthedocs.org/)
#
#==============================================================================

from gpiozero import Button
from subprocess import check_call
from signal import pause
from time import sleep

def shutdown():
	print ('Shuting Down!!')
	sleep(2)
	check_call(['sudo', 'poweroff'])
	

button_pwr = Button(21, hold_time=2)
button_pwr.when_held = shutdown


pause()

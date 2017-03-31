	#################################################################
##           SERVO LIB for SMART TOLLBOOTH PROJECT             ##
#################################################################

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

SERVO = 11

GPIO.setup(SERVO, GPIO.OUT)

def moveDeg(i):
	val = 0.001 + (i * 0.002 / 180)
	for x in range(400):
		GPIO.output(SERVO, GPIO.HIGH)
		time.sleep(val)
		GPIO.output(SERVO, GPIO.LOW)
		time.sleep(val)

def closeBarrier():
	moveDeg(0)

def openBarrier():
	moveDeg(90)

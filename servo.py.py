#!/usr/bin/env python
#servo.py
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
print("processing....")
p = GPIO.PWM(7, 50) # GPIO 7 for PWM with 50Hz
p.start(2.5) # Initialization
p.ChangeDutyCycle(2.5)
time.sleep(3)
p.ChangeDutyCycle(12.5)
time.sleep(3)
p.ChangeDutyCycle(2.5)
time.sleep(2)
p.stop()
time.sleep(20)
print("Completed!!")
time.sleep(1)
exit(0)
#Import necessary modules for turning on the LED light with GPIO signals
import RPi.GPIO as GPIO
import time

#Setting the mode to Broadcom number (actual pin number)
GPIO.setmode(GPIO.BCM)

#Setting up the pin to be a pin that outputs information
GPIO.setup(18, GPIO.OUT)

#Setting pin 18 to output a high signal
GPIO.output(18, GPIO.HIGH)
#Pause for three seconds
time.sleep(3)

#Setting pin 18 to output a low signal
GPIO.output(18, GPIO.LOW)
#Resetting the pin's statuses to their default states
#so that the next program that runs comes into a state that it expects
GPIO.cleanup()

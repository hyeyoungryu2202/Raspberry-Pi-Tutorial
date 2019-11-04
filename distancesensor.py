#Import necessary modules for measuring distance with the distance sensor
import RPi.GPIO as GPIO
import time

#Setting the mode to Broadcom number ("actual" pin number)
GPIO.setmode(GPIO.BCM)

#Define TRIG and ECHO as the Broadcom pin numbers
#that we intend to use for that part of the sensor
TRIG = 4
ECHO = 18

#Setting up the pin to be a pin that outputs information
GPIO.setup(TRIG, GPIO.OUT)
#Setting up the pin to be a pin that inputs information
GPIO.setup(ECHO, GPIO.IN)

#Issuing a signal out
GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)
while GPIO.input(ECHO) == False:
    start = time.time()

#When signal ends, retrieve the input time
while GPIO.input(ECHO) == True:
    end = time.time()
#Signal time is calculated as end time - start time
sig_time = end - start

#Distance is measured in centimeters
distance = sig_time / 0.000058

#Print the distance
print('Distance: {} centimeters'.format(distance))

#Resetting the pin's statuses to their default states
#so that the next program that runs comes into a state that it expects
GPIO.cleanup()

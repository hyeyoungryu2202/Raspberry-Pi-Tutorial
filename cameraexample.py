#Import necessary modules for Pi Camera module
import picamera
import time

camera = picamera.Picamera() #Define the camera object as camera
camera.capture('example.jpg') #.capture() snaps a quick photo

camera.vflip = True #Flips the camera vertifcally
#.hlip flips the camera horizontally

camera.capture('example 2.jpg')

camera.start_recording('examplevid.h264') #.start_recording records the video
time.sleep(5) #time.sleep() determines the recording duration
camera.stop_recording() #.stop_recording() stops recording the video

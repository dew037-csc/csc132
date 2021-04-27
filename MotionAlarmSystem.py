# import all needed imports
import RPi.GPIO as GPIO
from time import sleep
import pygame
from array import array
from gpiozero import MotionSensor
from signal import pause
from picamera import PiCamera


MIXER_FREQ = 44100
MIXER_SIZE = -16
MIXER_CHANS = 1
MIXER_BUFF = 1024

class Note(pygame.mixer.sound):
    def __init__(self, frequency, volume):
        self.freqeuncy = frequency
        pygame.mixer.Sound.__init__(self, buffer = self.build.samples())

    def build_samples(self):
        period = int(round(MIXER_FREQ / self.frequency))
        amplitude = 2 ** (abs(MIXER_SIZE -1) -1
        samples = array("h", [0] * period)

        for t in range(period):
            if(t < period / 2):
                samples[t] = amplitude
            else:
                samples[t] = -amplitude
        return(samples)



############################################################################################
# Main Program
################################################################################################
# set up camera module
def camera():
    camera = PiCamera()
    camera.resolution = (2592, 1944)
    print("Camera ready")
    sleep(0.1)
    camera.capture('/home/pi/Desktop/image.jpg')
                    
# set up motion sensor
motion_sensor = MotionSensor(4, threshold = 0.2)
def motion():
    print("Motion Detected")
    camera()

def no_motion():
    print("No Motion Detected")

print("Preparing Sensor...")
motion_sensor.wait_for_no_motion()
print("Sensor is ready")


motion_sensor.when_motion = motion
motion_sensor.when_no_motion = no_motion

pause()


                    
                


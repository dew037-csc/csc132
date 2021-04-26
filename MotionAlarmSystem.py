# import all needed imports
import RPi.GPIO as GPIO
from time import sleep
import pygame
from array import array

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
                    
                


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


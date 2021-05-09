# import all needed imports
import RPi.GPIO as GPIO
from time import sleep
import pygame
from array import array
from gpiozero import MotionSensor
from picamera import PiCamera
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

samples = []

MIXER_FREQ = 44100
MIXER_SIZE = -16
MIXER_CHANS = 1
MIXER_BUFF = 1024

class Note(pygame.mixer.Sound):
    def __init__(self, frequency, volume):
        self.frequency = frequency
        pygame.mixer.Sound.__init__(self, buffer = self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(MIXER_FREQ / self.frequency))
        amplitude = 2 ** (abs(MIXER_SIZE) -1) -1
        global samples
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
# setup alarm sound
def makeSound():
    if __name__ == "__main__":
        pygame.mixer.pre_init(44100, -16, 1, 1024)
        pygame.init()
        note = Note(440, 1)
        note.play(-1)
        sleep(0.5)
        note.stop()

# setup email sender
def sendEmail():
    toaddr = "picameraspam@gmail.com"           # reciever
    me = "picameraspam@gmail.com"                    # sender
    subject = "Security Camera Alert"           # subject line

    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = me
    msg["To"] = toaddr
    msg.preamble = "text"

    part = MIMEBase("application", "octet-stream")
    part.set_payload(open("image.jpg", "rb").read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename = 'image.jpg'")
    msg.attach(part)

    
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(user = "picameraspam@gmail.com", password = "blong9191")
    s.sendmail(me, toaddr, msg.as_string())
    s.quit()
        
               
# set up camera module
def camera():
    camera = PiCamera()
    try:
        camera.resolution = (2592, 1944)
        camera.framerate = 15
        print("Camera ready")
        sleep(0.1)
        for i in range(5):
            camera.capture('/home/pi/Desktop/image.jpg')
        # picameraspam@gmail.com
        # password: blong9191
        #sendEmail()
    finally:
        camera.close()
                    
# set up motion sensor
motion_sensor = MotionSensor(4, threshold = 0.2)
def motion():
    print("Motion Detected")
    camera()
    makeSound()
    sendEmail()
    

def no_motion():
    print("No Motion Detected")

print("Preparing Sensor...")
motion_sensor.wait_for_no_motion()
print("Sensor is ready")

while True:
    motion_sensor.when_motion = motion
    motion_sensor.when_no_motion = no_motion

    



                    
                


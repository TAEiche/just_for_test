from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

def preview ():

    camera = PiCamera()
    camera.resolution = (1920,1080)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.OUT)
    GPIO.setup(27,GPIO.OUT)
    camera.start_preview()
    sleep(2)
    GPIO.output(17,GPIO.HIGH)
    sleep(2)
    GPIO.output(17,GPIO.LOW) 
    GPIO.output(27,GPIO.HIGH)
    sleep(2)
    GPIO.output(27,GPIO.LOW)
    sleep(2)
    camera.stop_preview()
    #camera.resolution = (1920, 1080)
    #camera.capture('/home/pi/Pictures/test1.png')

    pass

preview()

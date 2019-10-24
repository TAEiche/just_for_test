from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

def preview ():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17,GPIO.OUT) #LED 1
    GPIO.setup(27,GPIO.OUT) #LED 2

    camera = PiCamera()
    #camera.resolution = (640, 480)
    camera.resolution = (1920, 1080)
    GPIO.output(17,GPIO.HIGH)
    GPIO.output(27,GPIO.HIGH)
    camera.start_preview()
    sleep(60)
    camera.stop_preview()
    #camera.capture('/home/pi/Pictures/testview.png')
    GPIO.output(17,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)

    pass

preview()

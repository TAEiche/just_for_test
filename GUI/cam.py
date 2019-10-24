from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library




class Cam():
    def rotate_capture (self, last_name):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(17,GPIO.OUT) #LED 1
        GPIO.setup(27,GPIO.OUT) #LED 2
        GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        path = '/home/pi/Pictures/'
        camera = PiCamera()
        camera.rotation = 180
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(27,GPIO.HIGH)
        camera.start_preview()
        while True:
          buttonState = GPIO.input(22)
          if buttonState == False:
            camera.capture(path + last_name + '.png')
            camera.stop_preview()
            GPIO.output(17,GPIO.LOW)
            GPIO.output(27,GPIO.LOW)
            break
        image_path = path + last_name + '.png'
        return image_path

    def capture (self, last_name):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(17,GPIO.OUT) #LED 1
        GPIO.setup(27,GPIO.OUT) #LED 2
        GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        path = '/home/pi/Pictures/'
        camera = PiCamera()
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(27,GPIO.HIGH)
        camera.start_preview()
        while True:
          buttonState = GPIO.input(22)
          if buttonState == False:
            camera.capture(path + last_name + '.png')
            camera.stop_preview()
            GPIO.output(17,GPIO.LOW)
            GPIO.output(27,GPIO.LOW)
            break
        image_path = path + last_name + '.png'
        return image_path


#sleep(3)
#camera.capture(path + last_name + '.png')
#camera.stop_preview()

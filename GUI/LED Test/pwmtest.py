GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT) #LED 1
GPIO.setup(27,GPIO.OUT) #LED 2
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
path = '/home/pi/Pictures/'
camera = PiCamera()
pwm1 = GPIO.PWM(17, 50)
pwm2 = GPIO.PWM(27, 50)
pwm1.start = 50
pwm2.start = 50
camera.start_preview()
while True:
  buttonState = GPIO.input(22)
  if buttonState == False:
    camera.capture(path + last_name + '.png')
    camera.stop_preview()
    pwm1.stop()
    pwm2.stop()
    break
image_path = path + last_name + '.png'
return image_path

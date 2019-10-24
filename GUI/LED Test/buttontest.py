import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
  buttonState = GPIO.input(15)
  if buttonState == False:
    print("come on baby")
  else:
    print("press me")

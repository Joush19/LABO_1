import RPi.GPIO as GPIO
import time

led1 = 12
led2 = 13
button = 15

counter = 1

GPIO.setwarning(False)

GPIO.setmode(GPIO.BCM)

def increase(channel):
    counter += 1

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(button, GPIO.RISING, callback=increase, bouncetime=50)

while True:
	if counter > 4:
		counter = 1
		
	if counter == 1:
		GPIO.output(led1, GPIO.LOW)
		GPIO.output(led2, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(led1, GPIO.HIGH)
		GPIO.output(led2, GPIO.LOW)
		time.sleep(1)
	
	elif counter == 2:
		GPIO.output(led1, GPIO.HIGH)
		GPIO.output(led2, GPIO.HIGH)
		time.sleep(2)
		GPIO.output(led1, GPIO.LOW)
		GPIO.output(led2, GPIO.LOW)
		time.sleep(2)
	
	elif counter == 3:
		GPIO.output(led1, GPIO.HIGH)
		GPIO.output(led2, GPIO.HIGH)

	elif counter == 4:
		GPIO.output(led1, GPIO.LOW)
		GPIO.output(led1, GPIO.LOW)


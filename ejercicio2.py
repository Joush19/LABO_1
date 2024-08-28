import RPi.GPIO as GPIO
import time

led = [9,10,11,12]
button = [15,16]

counter = 0

GPIO.setwarning(False)

GPIO.setmode(GPIO.BCM)

def increase(channel):
    counter += 1

def decrease(channel):
    counter -= 1

def convertb(num):
    format(num, '04b')

def convertx(num):
    format(num, '01x')

GPIO.setup(led,GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(button[0], GPIO.RISING, callback=increase, bouncetime=50)
GPIO.add_event_detect(button[1], GPIO.RISING, callback=increase, bouncetime=50)

while True:
    if (counter < 0) or (counter > 15):
        counter = 0

    bin = convertb(counter)
    hex = convertx(counter)

    GPIO.output(led[0], int(bin[0]))
    GPIO.output(led[1], int(bin[1]))
    GPIO.output(led[2], int(bin[2]))
    GPIO.output(led[3], int(bin[3]))
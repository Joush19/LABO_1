import RPi.GPIO as GPIO
import time

leds = [14,15,17,18]

button = [3,4]

count1 = 0
count2 = 1

selec = [1,1,1,1]

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

def increasec(channel):
    global count1, count2
    count1 += 1
    count2 = 1

def increaset(channel):
    global count2
    count2 += 1

GPIO.setup(leds, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(button[0], GPIO.FALLING, callback=increasec, bouncetime=300)
GPIO.add_event_detect(button[1], GPIO.FALLING, callback=increaset, bouncetime=300)

while True:

    if count1 > 3:
        count1 = 0

    GPIO.output(leds[count1], GPIO.HIGH)
    time.sleep(count2)
    GPIO.output(leds[count1], GPIO.LOW)
    time.sleep(1)


import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import random

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 8
fan = 9
led = 10

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(fan, GPIO.OUT)

while True:
    #h, t = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    t = random.randint(10,25)
    if t < 12:
        GPIO.output(led, 1)
    else:
        GPIO.output(led, 0)
    if t > 20:
        GPIO.output(fan, 1)
    else:
        GPIO.output(fan, 0)
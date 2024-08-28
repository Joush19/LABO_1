import RPi.GPIO as GPIO
import time

led_pin = 12

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)
#GPIO.setup(button_pin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led_pin, GPIO.LOW)
    time.sleep(1)

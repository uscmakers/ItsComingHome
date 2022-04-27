from webapp.spark import SparkController
import RPi.GPIO as GPIO          
from time import sleep

pwm_pin = 10

GPIO.setmode(GPIO.BCM)
controller = SparkController(pwm_pin)
sleep(1)
controller.set_speed(0.1)
sleep(2)
controller.nuetral()
sleep(1)

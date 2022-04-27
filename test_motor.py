from webapp.spark import SparkController
import RPi.GPIO as GPIO          
from time import sleep

pwm_pin = 13

GPIO.setmode(GPIO.BCM)
controller = SparkController(pwm_pin)
sleep(2)
print('Forward')
controller.set_speed(1)
sleep(2)
print('Neutral')
controller.neutral()
sleep(2)
print('Backwards')
controller.set_speed(-1)
sleep(2)
print('Neutral')
controller.set_speed(0)
sleep(2)


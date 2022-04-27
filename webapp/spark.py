import RPi.GPIO as GPIO

class SparkController:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 50)
        self.pwm.start(7.5)

    def nuetral(self):
        self.pwm.start(7.5)
    
    # Speed should be a value -1 to 1
    def set_speed(self, speed):
        self.pwm.start(7.5 + speed * 2.5)

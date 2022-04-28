import RPi.GPIO as GPIO

neutral_value = 7.12
speed_coefficient = 2.5

class SparkController:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 50)
        self.neutral()

    def neutral(self):
        self.pwm.start(neutral_value)
    
    # Speed should be a value -1 to 1
    def set_speed(self, speed):
        speed = min(max(speed, -1.0), 1.0)
        self.pwm.start(neutral_value + speed * speed_coefficient)

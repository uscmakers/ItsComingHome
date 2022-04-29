from flask import Flask, render_template, redirect, url_for
import RPi.GPIO as GPIO
from time import sleep
import spark as spark_module
from enum import Enum

class Direction(Enum):
    NONE = 0
    LEFT = 1
    CENTER = 2
    RIGHT = 3

in1 = 24
in2 = 23
pwm_pin = 13

move_speed = 0.25
move_wait = 0.5

position = Direction.NONE

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fire')
def fire():
    print('Fire!!!')
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    sleep(3)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/reset')
def reset():
    global position
    spark = spark_module.SparkController(pwm_pin)
    spark.set_speed(0.2)
    sleep(10)
    position = Direction.RIGHT
    spark.neutral()
    return redirect(url_for('index'))

@app.route('/left')
def left():
    global position
    spark = spark_module.SparkController(pwm_pin)
    if position == Direction.RIGHT:
        spark.set_speed(move_speed)
        sleep(2*move_wait)
        position = Direction.LEFT
    elif position == Direction.CENTER:
        spark.set_speed(move_speed)
        sleep(move_wait)
        position = Direction.LEFT
    spark.neutral()
    return redirect(url_for('index'))

@app.route('/center')
def center():
    global position
    spark = spark_module.SparkController(pwm_pin)
    if position == Direction.LEFT:
        spark.set_speed(move_speed)
        sleep(move_wait)
        position = Direction.CENTER
    elif position == Direction.RIGHT:
        spark.set_speed(-move_speed)
        sleep(move_wait)
        position = Direction.CENTER
    spark.neutral()
    return redirect(url_for('index'))

@app.route('/right')
def right():
    global position
    spark = spark_module.SparkController(pwm_pin)
    if position == Direction.LEFT:
        spark.set_speed(-move_speed)
        sleep(2*move_wait)
        position = Direction.RIGHT
    elif position == Direction.CENTER:
        spark.set_speed(-move_speed)
        sleep(move_wait)
        position = Direction.RIGHT
    spark.neutral()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')

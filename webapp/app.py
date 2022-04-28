from pickle import NONE
from flask import Flask, render_template, redirect, url_for
import RPi.GPIO as GPIO          
from time import sleep
from flask import g
from .spark import SparkController

from enum import Enum

class Direction(Enum):
    NONE = 0
    LEFT = 1
    CENTER = 2
    RIGHT = 3


in1 = 24
in2 = 23
pwm_pin = 13

move_speed = 0.3
move_wait = 2

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
    g.spark.set_speed(-0.2)
    sleep(10)
    g.position = Direction.RIGHT
    g.spark.neutral()
    return redirect(url_for('index'))

@app.route('/left')
def left():
    if g.position == Direction.RIGHT:
        g.spark.set_speed(move_speed)
        sleep(2*move_wait)
        g.position = Direction.LEFT
    elif g.position == Direction.CENTER:
        g.spark.set_speed(move_speed)
        sleep(move_wait)
        g.position = Direction.LEFT
    g.spark.neutral()
    return redirect(url_for('index'))

@app.route('/center')
def center():
    if g.position == Direction.LEFT:
        g.spark.set_speed(-move_speed)
        sleep(move_wait)
        g.position = Direction.CENTER
    elif g.position == Direction.RIGHT:
        g.spark.set_speed(move_speed)
        sleep(move_wait)
        g.position = Direction.CENTER
    g.spark.neutral()
    return redirect(url_for('index'))

@app.route('/right')
def right():
    if g.position == Direction.LEFT:
        g.spark.set_speed(-move_speed)
        sleep(2*move_wait)
        g.position = Direction.RIGHT
    elif g.position == Direction.CENTER:
        g.spark.set_speed(-move_speed)
        sleep(move_wait)
        g.position = Direction.RIGHT
    g.spark.neutral()
    return redirect(url_for('index'))

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    g.spark = SparkController(13)
    g.position = Direction.NONE
    app.run(debug=True, host='0.0.0.0')

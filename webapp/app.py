from flask import Flask, render_template, redirect, url_for
import RPi.GPIO as GPIO          
from time import sleep

in1 = 24
in2 = 23

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

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    app.run(debug=True, host='0.0.0.0')

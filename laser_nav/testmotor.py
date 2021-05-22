import RPi.GPIO as GPIO          
from time import sleep

GPIO.setmode(GPIO.BCM)

ena = 26
in1 = 13#19
in2 = 19#13
in3 = 21
in4 = 20
enb = 16

class Motor:
    def __init__(self, in1, in2, en):
        self.in1 = in1
        self.in2 = in2
        self.en = en
        GPIO.setup(self.in1,GPIO.OUT)
        GPIO.setup(self.in2,GPIO.OUT)
        GPIO.setup(self.en,GPIO.OUT)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)



    def run(self, forward: int):
        if forward > 0:
            GPIO.output(self.in1, GPIO.HIGH)
            GPIO.output(self.in2, GPIO.LOW)
        elif forward < 0:
            GPIO.output(self.in1, GPIO.LOW)
            GPIO.output(self.in2, GPIO.HIGH)
        else:
            GPIO.output(self.in1, GPIO.LOW)
            GPIO.output(self.in2, GPIO.LOW)


    def stop(self):
        self.run(0)
        


motora = Motor(in1, in2, ena)
motorb = Motor(in3, in4, enb)

p = GPIO.PWM(ena, 7000)
p.start(100)

q = GPIO.PWM(enb, 7000)
q.start(100)

def right():
    motora.run(forward=1)
    motorb.run(forward=-1)

def left():
    motora.run(forward=-1)
    motorb.run(forward=1)

def run(forward):
    motora.run(forward)
    motorb.run(forward)

def stop():
    motora.stop()
    motorb.stop()



while True:
    x=input()
    if x == 'r':
        run(1)
    elif x == 's':
        stop()
    elif x == 'b':
        run(-1)
    elif x == 'l':
        p.ChangeDutyCycle(50)
        q.ChangeDutyCycle(50)
    elif x == 'h':
        p.ChangeDutyCycle(100)
        q.ChangeDutyCycle(100)

from RPi import GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ir1=17                                  #sensor input1
ir2=27                                  #sensor input2
ir3=22                                  #sensor input3
ir4=14                                  #sensor input4
GPIO.setup(ir1,GPIO.IN)
GPIO.setup(ir2,GPIO.IN)
GPIO.setup(ir3,GPIO.IN)
GPIO.setup(ir4,GPIO.IN)
GPIO.setup(2,GPIO.OUT)                  #street light 1
GPIO.setup(3,GPIO.OUT)                  #street light 2
GPIO.setup(5,GPIO.OUT)                  #street light 3
GPIO.setup(6,GPIO.OUT)                  #street light 4
GPIO.setup(7,GPIO.OUT)                  #street light 5
GPIO.output(2,GPIO.HIGH)
while(True):
    if GPIO.input(ir1)==GPIO.LOW:
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(2,GPIO.LOW)
    elif GPIO.input(ir2)==GPIO.LOW:
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(3,GPIO.LOW)
    elif GPIO.input(ir3)==GPIO.LOW:
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(5,GPIO.LOW)
    elif GPIO.input(ir4)==GPIO.LOW:
        GPIO.output(7,GPIO.HIGH)
        GPIO.output(6,GPIO.LOW)
    else:
        GPIO.output(2,GPIO.HIGH)
        GPIO.output(3,GPIO.LOW)
        GPIO.output(5,GPIO.LOW)
        GPIO.output(6,GPIO.LOW)
        GPIO.output(7,GPIO.LOW)
    
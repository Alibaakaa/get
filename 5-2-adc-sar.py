import RPi.GPIO as GPIO
import sys
import time
from time import sleep

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def tobinery(x):
    return [int (element) for element in bin(x)[2:].zfill(8)]

def adc():
    t = 0
    for i in range(7, -1, -1):
        t += 2**i
        GPIO.output(dac, tobinery(t))
        sleep(0.0000001)
        if GPIO.input(comp)==0:
            t-=2**i
    return t
    

try:
    while True:
        timer_b = time.time()
        t = adc()
        if t != 0:
            timer_e = time.time()
            times_msecs = (timer_e - timer_b) * 1000
            print(t, '{:.2f}v'.format(3.3*t/256))
            print('Время: {}'.format(times_msecs))
           
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

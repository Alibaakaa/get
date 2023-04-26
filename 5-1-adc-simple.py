import RPi.GPIO as GPIO
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
    for i in range(256):
        a = tobinery(i)
        GPIO.output(dac, a)
        compvalue = GPIO.input(comp)
        sleep(0.000001)
        if compvalue==0:
            return i

try:
    while True:
        timer_b = time.time()
        i=adc()
        if i!=0:
            timer_e = time.time()
            times_msecs = (timer_e - timer_b) * 1000
            print(i, '{:.2f}v'.format(3.3*i/256))
            print('Время: {}'.format(times_msecs))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

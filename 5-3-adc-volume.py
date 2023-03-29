import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def tobinery(x):
    return [int (element) for element in bin(x)[2:].zfill(8)]

def adc():
    t = 0
    for i in range(7, -1, -1):
        t += 2**i
        GPIO.output(dac, tobinery(t))
        sleep(0.0001)
        if GPIO.input(comp)==0:
            t-=2**i
    return t
    
def vol(x):
    x=int(x/256*10)
    m=[0]*8
    for i in range(x-1):
        m[i]=1
    return m

try:
    while True:
        t = adc()
        if t != 0:
            GPIO.output(leds, vol(t))
            print(t, '{:.2f}v'.format(3.3*t/256))
           
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

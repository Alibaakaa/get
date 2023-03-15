import RPi.GPIO as GPIO 
from time import sleep 

dac=[26, 19, 13, 6, 5, 11, 9, 10] 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(dac, GPIO.OUT) 

def tobinery(x, n):
    return [int (element) for element in bin(x)[2:].zfill(n)] 
 
try: 
    while (True): 
        x=input() 
        if not x.isdigit(): 
            print('input number') 
        t=int(x)/256/2 
        for i in range(256): 
            GPIO.output(dac, tobinery(i, 8)) 
            sleep(t) 
        for i in range(255, -1, -1): 
            GPIO.output(dac, tobinery(i, 8)) 
            sleep(t) 

finally: 
    GPIO.output(dac, 1) 
    GPIO.cleanup()

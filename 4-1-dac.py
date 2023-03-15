import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

def tobinery(x, n):
    return [int (element) for element in bin(x)[2:].zfill(n)]
try: 
    while (True):
        x = input()
        if x == 'q':
            sys.exit()
        elif x.isdigit() and int(x)%1 == 0 and 0 <= int(x) and int(x) <=255:
            GPIO.output(dac, tobinery(int(x), 8))
            print("{:.5f}".format(int(x)*3.3/256))
        elif not x.isdigit():
            print('1.input number 0-255')

except ValueError:
    print('2.input number 0-255')

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
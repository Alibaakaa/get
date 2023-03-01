import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 0, 1, 1, 1, 1, 1, 1]
GPIO.setup(dac, GPIO.OUT)

for i in range(8):
    GPIO.output(dac[i], number[i])

time.sleep(15)

GPIO.output(dac, 0)
GPIO.cleanup()
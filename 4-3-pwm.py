import RPi.GPIO as GPIO  

GPIO.setmode(GPIO.BCM) 

GPIO.setup(2, GPIO.OUT) 
dac=[26, 19, 13, 6, 5, 11, 9, 10] 

GPIO.setup(dac, GPIO.OUT, initial=GPIO.HIGH) 
pwm = GPIO.PWM(2, 1000) 
pwm.start(0) 
 
try: 
    while (True): 
        DutyCicle=int(input()) 
        pwm.ChangeDutyCycle(DutyCicle) 
        print("{:.4f}".format(DutyCicle*3.3/100)) 
finally: 
    GPIO.output(2, 0) 
    GPIO.output(dac, 0) 
    GPIO.cleanup()

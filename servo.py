import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)

pwm=GPIO.PWM(32, 50)
pwm.start(0)

i = 0
while(i<190):
    dc = (9*i)/180 + 1
    pwm.ChangeDutyCycle(dc) # left 0 deg position
    sleep(.1)
    i+=5


pwm.stop()
GPIO.cleanup()
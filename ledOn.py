#GPIO 
import RPi.GPIO as GPIO
import time                     # library for sleep function (delay)

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)          # pin declared as output


try:
    while True:

    if ()
    GPIO.output(12, GPIO.HIGH)
                    
except KeyboardInterrupt:       # program ended with Ctrl+C
    print("Except")
    
GPIO.cleanup()# needed to clean use of programimport RPi.GPIO as GPIO

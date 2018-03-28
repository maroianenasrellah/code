# coding:utf-8
#!/usr/bin/python
# System modules
#from requests import get
from queue import Queue
from threading import  Thread
import time,sys,socket,requests
import RPi.GPIO as GPIO
import threading
import queue
import logging
greenPin=18
redPin=23
bluePin=24
bluered=25


time_sleep_led=3

def turnOff(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)
    
def blink(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,True)
    
def redOn():
	blink(redPin)
	
def greenOn():
	blink(greenPin)   

def bluegreenOn():
	blink(bluePin)
	
def blueredOn():
	blink(bluered)	
	
	
def redOff():
	turnOff(redPin)
	
def greenOff():
	turnOff(greenPin)
	
def bluegreenOff():
	turnOff(bluePin)
	
def blueredOff():
	turnOff(bluered)
    
	
def LED_Blink(Kel_led):
    iLed = threading.local()
    iLed.i = 0
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(Kel_led, GPIO.OUT)
    while (iLed.i <= 15):
        GPIO.output(Kel_led, True)
        time.sleep(0.1)   
        GPIO.output(Kel_led, False)
        time.sleep(0.1)
        iLed.i = iLed.i + 1
        
#t4 = threading.Thread(name='t4',target=LED_Blink, args=(bluePin,))

#t5 = threading.Thread(name='t5',target=LED_Blink, args=(bluered,))

#t4.start()

#t5.start()
greenOn()  
time.sleep(time_sleep_led)
greenOff()

redOn()  
time.sleep(time_sleep_led)
redOff()

time.sleep(time_sleep_led)



time.sleep(time_sleep_led)

bluegreenOn()
time.sleep(time_sleep_led)
bluegreenOff()


time.sleep(time_sleep_led)

blueredOn()
time.sleep(time_sleep_led)
blueredOff()

GPIO.cleanup()
import RPi.GPIO as gpio                    #Import GPIO library
import time                                #Import time library
gpio.setwarnings(False)

TRIG = 8                                  #Associate pin 23 to TRIG
ECHO = 7                                  #Associate pin 24 to ECHO

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(24, gpio.OUT)
    gpio.setup(TRIG,gpio.OUT)                  #Set pin as GPIO out
    gpio.setup(ECHO,gpio.IN)                   #Set pin as GPIO in


def forward (sec):
    gpio.output(17, True)
    gpio.output(23, False)
    gpio.output(22, True)
    gpio.output(24, False)
    #turn()
    time.sleep(sec)
    

def measure_distance():
    gpio.output(TRIG, False)                 #Set TRIG as LOW

    time.sleep(0.2)                            #Delay of 2 seconds

    gpio.output(TRIG, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    gpio.output(TRIG, False)                 #Set TRIG as LOW

    while gpio.input(ECHO)==0:               #Check whether the ECHO is LOW
        pulse_start = time.time()              #Saves the last known time of LOW pulse

    while gpio.input(ECHO)==1:               #Check whether the ECHO is HIGH
        pulse_end = time.time()                #Saves the last known time of HIGH pulse 

    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
    distance = round(distance, 2)            #Round to two decimal points
    return distance

def turn(sec):
    gpio.output(17, True)
    gpio.output(23, False)
    gpio.output(22, False)
    gpio.output(24, False)
    time.sleep(sec)
    
try:
    init()
    while True:
        distance = measure_distance()
        if distance > 2 and distance < 30:      #Check whether the distance is within range
            print ("Distance:",distance - 0.5,"cm") #Print distance with 0.5 cm calibration
            turn(1)
        else:
            print ('Out of range')
            forward(0.5)   
finally:
    gpio.cleanup()

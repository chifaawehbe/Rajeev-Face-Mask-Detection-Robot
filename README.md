# Rajeev-Face-Mask-Detection-Robot
A face mask detection robot that goes around the room and detects a face. Whenever there is a person without mask it plays a sound 'Put your mask on'. 

Built using Raspberry Pi 3 and Omni wheels with H bridge.

There were used OpenCV library to detect a face and GPIO library to be able to control the motors

# Features
Walks around a room 
```
def init():
    gpio.setmode(gpio.BCM)

    gpio.setup(17, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(24, gpio.OUT)

def forward (sec):
    gpio.output(17, True)
    gpio.output(23, False)
    gpio.output(22, True)
    gpio.output(24, False)
    time.sleep(sec)

def backward (sec):
    gpio.output(17, False)
    gpio.output(23, True)
    gpio.output(22, False)
    gpio.output(24, True)
    time.sleep(sec)
    
init()
forward(8)
print("forward")
#backward(4)
print("backward")
gpio.cleanup()
```
Finds a person using Ultrasonic Sensor and distance measurement
```
try:
    init()
    while True:
        distance = measure_distance()
        if distance > 2 and distance < 200:      
            print ("Distance:",distance - 0.5,"cm") 
            turn(1)
        else:
            print ('Out of range')
            forward(3)  
```

Detecs a face
```
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')

```
Plays a sound
```
playsound('/home/mysisteristhebest/Documents/Cri/M1/robotics-session1/project/Rajeev123.wav')
```

# Requirements
Python 3.9
Linux, MacOS or Windows 

# Required Components
For code:
Raspberry Pi 4
16 GB microSD card with an install Raspberry Pi OS
Power supply/Keyboard/Mouse/Monitor/HDMI Cable (for your Raspberry Pi)
USB Webcam or Raspberry Pi Camera

For robot:
Omni wheels
DC Motors
F/M and M/M jumpers
Power Supply
H bridge
Ultrasonic Sensor

Libraries:
OpenCV
GPIO

# Installation
1. Install the latest version of Raspberry Pi OS on your microSD card from here: https://www.raspberrypi.com/software/
2. Install VNC Viewer to be able to connect Raspberry Pi using the IP address
3. Open Raspberry Pi Configuration on your computer and enable a Raspberry Pi Camera.
4. Open a terminal on your computer and install OpenCV library
5. Import GPIO library to be able to control the motors

# Schematics
![alt text](https://github.com/chifaawehbe/Rajeev-Face-Mask-Detection-Robot/blob/78950ed85cd2c202927d8ad143a243c9ef97b476/Schematics%20Face%20Mask%20robot.png)

# Detecting a face

# Challenges
1. Tensor Flow library could be installed only up to Python  3.7
2. Technical problems of the SD card of the Raspberry Pi
3. Measuring the distance
4. Building a hardware - positioning all the elements of the robot

# References
https://smprobotics.com/usa/face-mask-detection-robot/  -  Face Mask Detection Robot article
https://www.youtube.com/watch?v=GKE7ngh1lLs - Raspberry Pi based Face Mask Detection using OpenCV
https://www.tomshardware.com/how-to/raspberry-pi-face-mask-detector  -  How to Build a Face Mask Detector with Raspberry Pi
https://circuitdigest.com/microcontroller-projects/face-mask-detection-using-raspberry-pi-and-opencv  -  Face Mask Detection using Raspberry Pi and OpenCV
https://www.raspberrypi.com/software/  -  Raspberry Pi OS Raspbian
https://raspberrypi.stackexchange.com/questions/7088/playing-audio-files-with-python  -  Playing audio files with Python on Raspberry Pi
https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/  -  Using a Raspberry Pi distance sensor (ultrasonic sensor HC-SR04)

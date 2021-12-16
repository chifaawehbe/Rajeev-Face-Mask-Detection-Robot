# Rajeev-Face-Mask-Detection-Robot
A face mask detection robot that goes around the room and detects a face. Whenever there is a person without mask it plays a sound 'Put your mask on'. 

Built using Raspberry Pi 3 and Omni wheels with H bridge.

There were used OpenCV library to detect a face and GPIO library to be able to control the motors

# Features
Walks around a room 

Finds a person

Detecs a face
# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')

Plays a sound


# Requirements
Python 3.9
Linux, MacOS or Windows 

# Materials and Supplies
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

Libraries:
OpenCV
GPIO

# Installation
1. Install the latest version of Raspberry Pi OS on your microSD card from here: https://www.raspberrypi.com/software/
2. Install VNC Viewer to be able to connect Raspberry Pi using the IP address
3. Open Raspberry Pi Configuration on your computer and enable a Raspberry Pi Camera.
4. Open a terminal on your computer and install OpenCV library
5. Import GPIO library to be able to control the motors




# virtual-telepresence-robot
A telepresence robot is a remote-controlled, wheeled device with a cameras to enable video conferencing and 
give the appearance of being present at place other than their true location. It is possible with combination of virtual reality and
IOT using Raspberry pi. Major 3 components of this project are controlling pc for driving robot , mobile for VR and head movement tracking
and the actual robot which has camera and pan-tilt head.
## Block diagram
![alt text](https://user-images.githubusercontent.com/30182047/28226367-7ba58d98-68f3-11e7-8f96-43250bc98188.png)

### Hardware used
- 2 Raspberry pi with memory card 
- 2 motor drivers L293D one for controlling car and another for vertical lift
- self-made vertical lift using 8mm threaded rod n bolt connected to motor
- 5 motors
- 1 or 2 camera (we used Logitech 310 )
- pan tilt bracket
- servomotor  
- virtual reality headset

### Software used
- UV4L & servoblaster installed on raspberry pi
- wireless IMU android app  
- self-made VTR android app for virtual reality headset can be configured for single or dual camera (for 3D) visuals.

#### softeware installation
* Self-made python script for robot car control

* Refer (https://github.com/epiception/Virtual-Telepresence/blob/master/Surrogates/Python-Code/Python-Code-version1.0/servo_blasteroid.py ) 
for head movement tracking

* UV4L installation (https://www.linux-projects.org/uv4l/)

* Servoblaster installation (https://github.com/BioMachinesLab/drones/wiki/Installing-Servoblaster)

* Wireless imu app (https://play.google.com/store/apps/details?id=org.zwiener.wimu&hl=en)

* Self-made virtual telepresence robot (VTR) android app
#### VTR.apk
![alt text](https://user-images.githubusercontent.com/30182047/28227810-4978273a-68f9-11e7-889e-2335331983c9.png) ![alt text](https://user-images.githubusercontent.com/30182047/28227821-5b2c9f24-68f9-11e7-81ba-6db08b073f86.png) 


## Virtual Telepresence Robot
![alt text](https://user-images.githubusercontent.com/30182047/28226851-3ad12410-68f5-11e7-856a-dc38d34e6575.jpeg)

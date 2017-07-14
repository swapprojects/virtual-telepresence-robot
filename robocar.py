# robot and vertical lift control program
#!/usr/local/bin/ env python
# date 20170702 04:36 PM
import RPi.GPIO as io
io.setmode(io.BCM)
import os
os.system('sudo pigpiod')
# set variables Motor speed.
motorLspeed = 20
motorRspeed = 20
maxspeed = 40
minspeed = 0
speedstep = 5
# set variable actual direction
direction = " "
# set variable for turning on spot
spot = "false"
# Here we configure the PWM settings for
# the four DC motors. It defines the two GPIO
# pins used for the input on the L298 H-Bridge,
# starts the PWM and sets the
# motors speed initial to 0

motor1_in1_pin = 27
motor1_in2_pin = 22
io.setup(motor1_in1_pin, io.OUT)
io.setup(motor1_in2_pin, io.OUT)


motor2_in1_pin = 13
motor2_in2_pin = 6
io.setup(motor2_in1_pin, io.OUT)
io.setup(motor2_in2_pin, io.OUT)


motor3_in1_pin = 21
motor3_in2_pin = 20
io.setup(motor3_in1_pin, io.OUT)
io.setup(motor3_in2_pin, io.OUT)


# set PWM for motor1 to 0
motorpwm1_in1_pin = 4
motorpwm1_in2_pin = 17
io.setup(motorpwm1_in1_pin, io.OUT)
io.setup(motorpwm1_in2_pin, io.OUT)
motorpwm1 = io.PWM(4,100)
motorpwm1 = io.PWM(17,100)
motorpwm1.start(0)
motorpwm1.ChangeDutyCycle(20)


# set PWM for motor2 to 0
motorpwm2_in1_pin = 18
motorpwm2_in2_pin = 23
io.setup(motorpwm2_in1_pin, io.OUT)
io.setup(motorpwm2_in2_pin, io.OUT)
motorpwm2 = io.PWM(18,100)
motorpwm2 = io.PWM(23,100)
motorpwm2.start(0)
motorpwm2.ChangeDutyCycle(20)

# The catch method can determine which key has been pressed
# by the user on the keyboard.
def getch() :
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
try:
tty.setraw(sys.stdin.fileno())
ch = sys.stdin.read(1)
finally:
termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
return ch

# Here we define the methods used to determine
# whether a motor needs to spin forward or backwards.
# both pins match, the motor will not turn.

def reverse():
io.output(motor1_in1_pin, False)
io.output(motor1_in2_pin, True)
io.output(motor2_in1_pin, False)
io.output(motor2_in2_pin, True)
print ("Reverse direction")

def forward():
io.output(motor1_in1_pin,  True)
io.output(motor1_in2_pin,False)
io.output(motor2_in1_pin, True)
io.output(motor2_in2_pin, False)
print ("Forword direction")

# stop the motors
def stop():
io.output(motor1_in1_pin, False)
io.output(motor1_in2_pin, False)
io.output(motor2_in1_pin, False)
io.output(motor2_in2_pin, False)
io.output(motor3_in1_pin, False)
io.output(motor3_in2_pin, False)
motorLspeed = 0
motorRspeed = 0
acceleration = 0

def left():
io.output(motor1_in1_pin,  True)
io.output(motor1_in2_pin,False)
io.output(motor2_in1_pin, False)
io.output(motor2_in2_pin, False)
print ("Left direction")

def right():
io.output(motor1_in1_pin,  False)
io.output(motor1_in2_pin,False)
io.output(motor2_in1_pin, True)
io.output(motor2_in2_pin, False)
print ("Rights direction")

def rotate():
io.output(motor1_in1_pin,  True)
io.output(motor1_in2_pin,False)
io.output(motor2_in1_pin, False)
io.output(motor2_in2_pin, True)
print ("Rotate")

def liftup():
io.output(motor3_in1_pin,  True)
io.output(motor3_in2_pin,False)
print ("Lift up")

def liftdown():
io.output(motor3_in1_pin, False)
io.output(motor3_in2_pin,True)
print ("Lift down")

def check_motorpseed(motorLspeed, motorRspeed):

if (motorLspeed < minspeed):
motorLspeed = minspeed
if (motorLspeed > maxspeed):
motorLspeed = maxspeed

if (motorRspeed < minspeed):
motorRspeed = minspeed
if (motorRspeed > maxspeed):
motorRspeed = maxspeed

return motorLspeed, motorRspeed

# Instructions for when the user has an interface
print("w/s: direction")
print("a/d: steering")
print("q: stops the motors")
print("x: exit")

# Infinite loop
# The loop will not end until the user presses the
# exit key ‘X’ or the program crashes…
while True:
# Keyboard character retrieval method. This method will save
# the pressed key into the variable char
char = getch()
x=(motorLspeed+motorRspeed)/2
print ("speed :  "+str(x))
# The car will drive forward when the “w” key is pressed
if(char == "w"):
forward()

sleep(0.1)
stop()
# The car will reverse when the “s” key is pressed
if(char == "s"):
reverse()
sleep(0.1)
stop()

# Stop the motors
if(char == "q"):
stop()
motorRspeed = 20

motorLspeed = 2
print ("STOP")

# The “d” key will toggle the steering right
if(char == "d"):
right()
sleep(0.1)
stop()

# The “a” key will toggle the steering left
if(char == "a"):
left()
sleep(0.1)
stop()
if(char == "e"):
rotate()
sleep(0.1)
stop()
if(char == "r"):

motorRspeed = motorRspeed + speedstep
motorLspeed = motorLspeed + speedstep
motorpwm1.ChangeDutyCycle(motorLspeed)
motorpwm2.ChangeDutyCycle(motorRspeed)



if(char == "f"):
motorRspeed = motorRspeed - speedstep
motorLspeed = motorLspeed - speedstep
motorpwm1.ChangeDutyCycle(motorLspeed)
motorpwm2.ChangeDutyCycle(motorRspeed)

if(char == "t"):
liftup()
sleep(0.1)
stop()

if(char == "g"):
liftdown()
sleep(0.1)
stop()
# The “x” key will break the loop and exit the program
if(char == "x"):
print("Program Ended")
break

# The keyboard character variable char has to be set blank. We need
# to set it blank to save the next key pressed by the user
char = ""
# Program will clean up all GPIO settings and terminates
io.cleanup()
# End

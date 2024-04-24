from imu import MPU6050
import time
from machine import Pin, I2C
from math import atan2, degrees
from motor import Motor
from control_loop import ControlLoop

#Shows Pi is on by turning on LED when plugged in
#Shows Pi is on by turning on LED when plugged in
LED = machine.Pin("LED", machine.Pin.OUT)
LED.on()


##################################################
#INPUT/OUTPUT MAPPING
##################################################
MOTORLEFT_IN_1 = 27
MOTORLEFT_IN_2 = 28
MOTORLEFT_EN = 14

MOTORRIGHT_IN_1 = 22
MOTORRIGHT_IN_2 = 26
MOTORRIGHT_EN = 15

RobotStateMachine = {"SoftStop" : 0, "Auto" : 10, "TeleOp" : 20}
ControlStateMachine = {"Hover" : 0, "Forward" : 10, "Reverse" : 20, "TurnRight" : 30, \
"Turn Left" : 40}

RobotState = RobotStateMachine["Auto"]
ControlState = ControlStateMachine["Hover"]


def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle




i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(i2c)

Robot = ControlLoop()
Robot.MotorLeft = Motor(MOTORLEFT_IN_1, MOTORLEFT_IN_2, MOTORLEFT_EN)
Robot.MotorRight = Motor(MOTORRIGHT_IN_1, MOTORRIGHT_IN_2, MOTORRIGHT_EN)




try:
    while True:

        #########################
        # LOOP INPUTS           #
        #########################

        #calculate imu properties
        ax = imu.accel.x
        #ay = imu.accel.y
        az = imu.accel.z
        #gx = imu.gyro.x
        #gy = imu.gyro.y
        #gz = imu.gyro.z

        #Use acceleration to retrieve inclination
        XZ = vector_2_degrees(ax, az)
        #YZ =  vector_2_degrees(ay, az)

        Robot.ReferencePoint = XZ
        
        #########################
        # STATE HANDLER         #
        #########################
        # Protect robot by shutting down motors .
       
        if Robot.ReferencePoint < Robot.ReverseLimit and Robot.ReferencePoint < Robot.ForwardLimit \
           or Robot.ReferencePoint > Robot.ForwardLimit and Robot.ReferencePoint > Robot.ReverseLimit:
            RobotState = RobotStateMachine["SoftStop"]
        else:
            RobotState = RobotStateMachine["Auto"]
       
        # add handler to switch between auto and teleop


        #########################
        # STATE MACHINE         #
        #########################
        if RobotState == RobotStateMachine["SoftStop"]:
            Robot.Stop()

        elif RobotState == RobotStateMachine["Auto"]:
            if ControlState == ControlStateMachine["Hover"]:
                Robot.Balance()
            
        elif RobotState == RobotStateMachine["TeleOp"]:
            pass
except Exception as err:
    Robot.Stop()
    led = Pin(25, Pin.OUT)
    print("He's Dead Jim: " + err)
    while True:
        led.toggle()
        time.sleep(1)

      



    #print(f"Angle is ({XZ})")









#Shows Pi is on by turning on LED when plugged in
LED = machine.Pin("LED", machine.Pin.OUT)
LED.on()


from imu import MPU6050
from time import sleep
from machine import Pin, I2C
from math import atan2, degrees
from motor import Motor
from control_loop import ControlLoop


##################################################
#INPUT/OUTPUT MAPPING
##################################################
MOTORLEFT_IN_1 = 27
MOTORLEFT_IN_2 = 28
MOTORLEFT_EN = 13

MOTORRIGHT_IN_1 = 22
MOTORRIGHT_IN_2 = 26
MOTORRIGHT_EN = 15

dict RobotStateMachine ["SoftStop" : 0, "Auto" : 10, "TeleOp" : 20]
dict ControlStateMachine["Hover" : 0, "Forward" : 10, "Reverse" : 20, "TurnRight" : 30, \
"Turn Left" : 40]

RobotState = RobotStateMachine["SoftStop"]
ControlState = ControlStateMachine["Hover"]


def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle




i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(i2c)


MotorLeft = Motor(MOTORLEFT_IN_1, MOTORLEFT_IN_2, MOTORLEFT_EN)
MotorRight = Motor(MOTORRIGHT_IN_1, MOTORRIGHT_IN_2, MOTORRIGHT_EN)

Robot = ControlLoop(MotorLeft, MotorRight)


while True:

    #########################
    # LOOP INPUTS           #
    #########################

    #calculate imu properties
    ax = imu.accel.x
    ay = imu.accel.y
    az = imu.accel.z
    gx = imu.gyro.x
    gy = imu.gyro.y
    gz = imu.gyro.z

    #Use acceleration to retrieve inclination
    XZ = vector_2_degrees(ax, az)
    YZ =  vector_2_degrees(ay, az)

    #########################
    # STATE HANDLER         #
    #########################
    # Protect robot by shutting down motors .
    if Robot.ReferencePoint < Robot.ReverseLimit or Robot.ReferencePoint > self.ForwardLimit:
        RobotState = RobotStateMachine["SoftStop"] 
    
    # add handler to switch between auto and teleop


    #########################
    # STATE MACHINE         #
    #########################
    if RobotState = RobotStateMachine["SoftStop"]
        Robot.Stop()

    elif RobotState = RobotStateMachine["Auto"]:
        pass
        
    elif RobotState = RobotStateMachine["TeleOp"]:
        pass


  



    print(f"Angle is ({XZ}, {YZ})")



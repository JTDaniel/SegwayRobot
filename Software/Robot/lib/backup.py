#Shows Pi is on by turning on LED when plugged in
LED = machine.Pin("LED", machine.Pin.OUT)
LED.on()


from imu import MPU6050
from machine import Pin, I2C
from math import atan2, degrees
from motor import Motor
from control_loop import ControlLoop
from ping import UltraSonic
import _thread
import time


def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle

def obstacle_thread(sensor1, sensor2):
    result = [sensor1.obstacleDetected(), sensor2.obstacleDetected()]
    #print(result)
    return result


##################################################
#INPUT/OUTPUT MAPPING
##################################################
MOTORLEFT_IN_1 = 27
MOTORLEFT_IN_2 = 28
MOTORLEFT_EN = 14
MOTORLEFT_A = 21
MOTORLEFT_B = 20

MOTORRIGHT_IN_1 = 22
MOTORRIGHT_IN_2 = 26
MOTORRIGHT_EN = 15
MOTORRIGHT_A = 21
MOTORRIGHT_B = 20

RobotStateMachine = {"SoftStop" : 0, "Auto" : 10, "TeleOp" : 20}
ControlStateMachine = {"Hover" : 0, "Forward" : 10, "Reverse" : 20, "TurnRight" : 30, \
"TurnLeft" : 40}

RobotState = RobotStateMachine["Auto"]
ControlState = ControlStateMachine["Hover"]

HOVER_TIME = 10 #seconds before moving

##################################################
# Instantiate Robot, Sensors, and Motors
##################################################
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(i2c)
Robot = ControlLoop()
Robot.MotorLeft = Motor(MOTORLEFT_IN_1, MOTORLEFT_IN_2, MOTORLEFT_EN, MOTORLEFT_A, MOTORLEFT_B)
Robot.MotorRight = Motor(MOTORRIGHT_IN_1, MOTORRIGHT_IN_2, MOTORRIGHT_EN, MOTORRIGHT_A, MOTORRIGHT_B)
Ping = [UltraSonic(13,12), UltraSonic(9,8)]

_thread.start_new_thread(obstacle_thread, Ping)

historian = []
n = 10

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


    historian.append(XZ)
    try:
        myHistorian = historian[-(n):]
    except:
        myHistorian = historian[:]
    if len(historian) > n: historian.pop(0)
    Robot.ReferencePoint = sum(myHistorian)/len(myHistorian)
 
        


    if(Robot.MotorLeft.count) >1: break
    try:
        detected = _thread.start_new_thread(obstacle_thread, Ping)
    except OSError:
        pass
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
    #if ControlState != ControlStateMachine["Hover"]: hoverStartTime = time.time()
    #if ControlState == ControlState["Hover"]: avoidStartTime = time.time()
    if RobotState == RobotStateMachine["SoftStop"]:
        Robot.Stop()

    elif RobotState == RobotStateMachine["Auto"]:
        
        
        if ControlState == ControlStateMachine["Hover"]: 
            #hoverElapsedTime = time.time() - hoverStartTime
            Robot.Balance()
            # if hoverElapsedTime > HOVER_TIME:
            #     ControlState = ControlStateMachine["Forward"]

        
       #if Ping[1].obstacleDetected():
        #    ControlState = ControlStateMachine["TurnLeft"]
         #   print("Obstacle Detected On Right!")
        if ControlState == ControlStateMachine["TurnLeft"]:
            #avoidElapsedTime = time.time() - avoidStartTime
            Robot.TurnLeft()
            #if avoidElapsedTime > 3: ControlState = ControlStateMachine["Hover"]
      
        # if UltraSonic[1].obstacleDetected(): ControlState = ControlStateMachine["Reverse"]
        # if ControlState == ControlStateMachine["Reverse"]:
        #     avoidElapsedTime = time.time() - avoidStartTime
        #     Robot.MoveBackward()
        #     if avoidElapsedTime > 3: ControlState = ControlStateMachine["Hover"]
           

        #if Ping[0].obstacleDetected():
         #   ControlState = ControlStateMachine["TurnRight"]
          #  print("Obstacle Detected On Left!")
        if ControlState == ControlStateMachine["TurnRight"]:
            #avoidElapsedTime = time.time() - avoidStartTime
            Robot.TurnRight()
            #if avoidElapsedTime > 3: ControlState = ControlStateMachine["Hover"]

        
    elif RobotState == RobotStateMachine["TeleOp"]:
        pass


  















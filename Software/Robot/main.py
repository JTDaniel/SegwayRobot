#Shows Pi is on by turning on LED when plugged in
LED = machine.Pin("LED", machine.Pin.OUT)
LED.on()


from imu import MPU6050
from time import sleep
from machine import Pin, I2C
from math import atan2, degrees
from motor import Motor


##################################################
#INPUT/OUTPUT MAPPING
##################################################
MOTORLEFT_IN_1 = 27
MOTORLEFT_IN_2 = 28
MOTORLEFT_EN = 13

MOTORRIGHT_IN_1 = 22
MOTORRIGHT_IN_2 = 26
MOTORRIGHT_EN = 15





def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle




i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(i2c)

MotorLeft = Motor(MOTORLEFT_IN_1, MOTORLEFT_IN_2, MOTORLEFT_EN)
MotorRight = Motor(MOTORRIGHT_IN_1, MOTORRIGHT_IN_2, MOTORRIGHT_EN)


while True:
    ax=round(imu.accel.x,2)
    ay=round(imu.accel.y,2)
    az=round(imu.accel.z,2)
    gx=round(imu.gyro.x)
    gy=round(imu.gyro.y)
    gz=round(imu.gyro.z)

    XZ = vector_2_degrees(ax, az)
    YZ =  vector_2_degrees(ay, az)


    if XZ < 90:
        MotorLeft.DriveForward(MotorLeft.MAX_FREQ)
        MotorRight.DriveReverse(MotorRight.MAX_FREQ)
    elif XZ > 90:
        MotorLeft.DriveReverse(MotorLeft.MAX_FREQ)
        MotorRight.DriveForward(MotorRight.MAX_FREQ)


    print(f"Angle is ({XZ}, {YZ})")

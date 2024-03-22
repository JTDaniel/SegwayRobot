##################################################
#Class file to define motor object and functions
##################################################
from machine import Pin, PWM

ON = 1
OFF = 0

class Motor():
    def __init__(self, In1, In2, En) -> None:

        self.MAX_FREQ = 65025
        self.MIN_FREQ = 0 
        self.P_In1 = Pin(In1, Pin.OUT)
        self.P_In2 = Pin(In2, Pin.OUT)
        self.P_En = PWM(Pin(En))
        self.P_En.freq(1000)


    def DriveForward(self, Speed) -> None:
        self.P_In1.value(ON)
        self.P_In2.value(OFF)
        self.P_En.duty_u16(Speed)

    def DriveReverse(self, Speed) -> None:
        self.P_In1.value(OFF)
        self.P_In2.value(ON)
        self.P_En.duty_u16(Speed)

    def Stop(self) -> None:
        self.P_In1.value(OFF)
        self.P_In2.value(OFF)
        self.P_En.duty_u16(self.MIN_FREQ)

    def EncoderCount() -> None:
        pass


    #Add ability to move by encoder counts.
    def MoveRelative() -> None:
        pass

    


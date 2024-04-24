##################################################
#Class file to define control loop object and functions
##################################################
from motor import Motor


class ControlLoop():
    
    def __init__(self) -> None:
        self.Vertical = 281
        self.ForwardLimit = self.Vertical - 50
        self.ReverseLimit = self.Vertical + 50
        self.Setpoint = self.Vertical
        self.P = 2500
        self.I = 50
        self.D = 0
        self.historian = []
        self.HISTORIAN_LIM = 100
        self.DEADZONE_FREQ = 35000
        self.ReferencePoint = None
        self.MotorLeft = None
        self.MotorRight = None


    def error(self, Setpoint, ReferencePoint) -> float:
        error = Setpoint - ReferencePoint
        return error

    #compensate for current error
    def Proportional(self, P) -> float:
        return self.error(self.Vertical, self.ReferencePoint) * P 

    #accumulate error from a time constant
    def Integral(self) -> float:
        self.historian.append(self.error(self.Vertical, self.ReferencePoint))
        try:
            myHistorian = self.historian[-self.I:]
        except:
            myHistorian = self.historian[:]
        if len(self.historian) > self.HISTORIAN_LIM: self.historian.pop(0)
        return sum(myHistorian)/len(myHistorian)
        

    #compensate for quick changes in error
    def Derivative(self) -> float:
        pass
        
    def Balance(self) -> None:
        motorSpeed = int(self.Proportional(self.P)) # +self.Integral + self.Derivatove
        motorSpeedAbs = abs(motorSpeed) + self.DEADZONE_FREQ
        if motorSpeed > 0:
            self.MotorLeft.DriveForward(motorSpeedAbs)
            self.MotorRight.DriveForward(motorSpeedAbs)
        elif motorSpeed <= 0:
            self.MotorLeft.DriveReverse(motorSpeedAbs)
            self.MotorRight.DriveReverse(motorSpeedAbs)
        print("Balancing" + motorSpeedAbs)
            
    def MoveForward(self) -> None:
        pass

    def MoveBackward(self) -> None:
        pass

    def TurnRight(self) -> None: 
        motorSpeed = int(self.Proportional(self.P)) # +self.Integral + self.Derivatove
        motorSpeedAbs = abs(motorSpeed) + self.DEADZONE_FREQ
        if motorSpeed > 0:
            self.MotorLeft.DriveForward(motorSpeedAbs)
            self.MotorRight.DriveForward(motorSpeedAbs)
        elif motorSpeed <= 0:
            self.MotorLeft.DriveReverse(motorSpeedAbs)
            self.MotorRight.DriveReverse(motorSpeedAbs)
        print("Turning Right " + motorSpeedAbs)

    def TurnLeft(self) -> None:
        motorSpeed = int(self.Proportional(self.P)) # +self.Integral + self.Derivatove
        motorSpeedAbs = abs(motorSpeed) + self.DEADZONE_FREQ
        if motorSpeed > 0:
            self.MotorLeft.DriveForward(motorSpeedAbs)
            self.MotorRight.DriveForward(motorSpeedAbs)
        elif motorSpeed <= 0:
            self.MotorLeft.DriveReverse(motorSpeedAbs)
            self.MotorRight.DriveReverse(motorSpeedAbs)
        print("Turning Left " + motorSpeedAbs)

    def Stop(self) -> None:
        self.MotorLeft.Stop()
        self.MotorRight.Stop()

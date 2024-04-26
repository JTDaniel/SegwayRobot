##################################################
#Class file to define control loop object and functions
##################################################
from motor import Motor


class ControlLoop():
    
    def __init__(self) -> None:
        self.Vertical = 280
        self.ForwardLimit = self.Vertical - 50
        self.ReverseLimit = self.Vertical + 50
        self.Setpoint = self.Vertical
        self.P = 3000
        self.I = 2000
        self.D = 0
        self.TS = 10
        self.historian = []
        self.HISTORIAN_LIM = 50
        self.DEADZONE_FREQ = 30000
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
    def Integral(self, I) -> float:
        self.historian.append(self.error(self.Vertical, self.ReferencePoint))
        try:
            myHistorian = self.historian[-(self.TS):]
        except:
            myHistorian = self.historian[:]
        if len(self.historian) > self.HISTORIAN_LIM: self.historian.pop(0)
        result = sum(myHistorian)/len(myHistorian)
        return result * I
        

    #compensate for quick changes in error
    def Derivative(self) -> float:
        return 0
        
    def Balance(self) -> None:
        motorSpeed = int(self.Proportional(self.P)) + int(self.Integral(self.I)) #+ self.Derivatove
        motorSpeedAbs = abs(motorSpeed) + self.DEADZONE_FREQ
        if motorSpeed > 0:
            self.MotorLeft.DriveForward(motorSpeedAbs)
            self.MotorRight.DriveForward(motorSpeedAbs)
        elif motorSpeed <= 0:
            self.MotorLeft.DriveReverse(motorSpeedAbs)
            self.MotorRight.DriveReverse(motorSpeedAbs)
        #print("Balancing " + str(motorSpeedAbs))
            
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
        #print("Turning Right " + str(motorSpeedAbs))

    def TurnLeft(self) -> None:
        motorSpeed = int(self.Proportional(self.P)) # +self.Integral + self.Derivatove
        motorSpeedAbs = abs(motorSpeed) + self.DEADZONE_FREQ
        if motorSpeed > 0:
            self.MotorLeft.DriveForward(motorSpeedAbs)
            self.MotorRight.DriveForward(motorSpeedAbs)
        elif motorSpeed <= 0:
            self.MotorLeft.DriveReverse(motorSpeedAbs)
            self.MotorRight.DriveReverse(motorSpeedAbs)
        #print("Turning Left " + str(motorSpeedAbs))

    def Stop(self) -> None:
        self.MotorLeft.Stop()
        self.MotorRight.Stop()


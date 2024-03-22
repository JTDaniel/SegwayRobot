##################################################
#Class file to define control loop object and functions
##################################################
from motor import Motor


class ControlLoop()
    
    def __init__(self) -> None:
        self.Vertical = 90
        self.ForwardLimit = self.Vertical - 15
        self.ReverseLimit = self.Vertical + 15
        self.Setpoint = self.Vertical
        Self.ReferencePoint = None

    def DefineMotors(self, MotorLeft, MotorRight)
        self.MotorLeft = MotorLeft
        self.MotorRight = MotorRight

    def error(self, Setpoint = self.Vertical, ReferencePoint = Self.ReferencePoint) -> float:
        return error = abs(Setpoint - ReferencePoint)

    def Proportional(self) -> float:
        pass

    def Integral(self) -> float:
        pass

    def Derivative(self) -> float:
        pass
        
    def Balance(self) -> None:
        pass

    def MoveForward(self) -> None:
        pass

    def MoveBackward(self) -> None:
        pass

    def TurnRight(self) -> None: 
        pass

    def TurnLeft(self) -> None:
        pass

    def Stop(self) -> None:
        self.MotorLeft.Stop()
        self.MotorRight.Stop()
##################################################
#Class file to define Ultrasonic object and functions
##################################################
from machine import Pin, time_pulse_us
import utime

ON = 1
OFF = 0

SOUND_SPEED = 340
PULSE_LENGTH = 5


class UltraSonic():
    def __init__(self, trigPin, echoPin) -> None:
        self.trig = Pin(trigPin, Pin.OUT)
        self.echo = Pin(echoPin, Pin.IN)
        
    def getDist(self):
        self.trig.low()
        utime.sleep_us(2)
        self.trig.high()
        utime.sleep_us(PULSE_LENGTH)
        self.trig.low()

        while self.echo.value() == 0: signaloff = utime.ticks_us()
        while self.echo.value() == 1: signalon = utime.ticks_us()
        
        duration = signalon - signaloff
        dist = (duration*0.0343)/2

        return dist
    
    def obstacleDetected(self):
        if self.getDist() < 20: return True
        else: return False


    if __name__ == "__main__":
        US = UltraSonic(12,13)
        while True:
            print(US.getDist)


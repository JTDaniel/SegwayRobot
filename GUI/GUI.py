import tkinter as tk
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

###########################################################################
# The below class will take care of the Robot Tilt Widget Fucntions.  This
# Will Read from Serial in order to get gyroscopic information from the 
# robot.
###########################################################################
class RobotTilt():
    def __init__(self) -> None:
        pass

    def readGyro() -> dict:
        pass

###########################################################################
# The Below Class will take care of the PID Graphic,  it will show the 
# graphic POC/PID.png as well as show the PID magnitudes as sliders. These
# sliders will be user operable
###########################################################################
class PID():
    def __init__(self) -> None:
        pass

###########################################################################
# The below class will take care of the obstacle detection map.  This map 
# This map will grab pips everytime an obstacle is detected (with a LPF)
# and plot them on a canvas.
###########################################################################
class ObstacleDetectionMap():
    def __init__(self) -> None:
        pass

if __name__ == "__main__":
    root = tk.Tk()
    root.title("SegWay Robot Client")
    mainframe = tk.Frame(master= root)

    


    root.mainloop()

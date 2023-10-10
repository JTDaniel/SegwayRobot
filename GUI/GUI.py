import tkinter as tk
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

###########################################################################
# The below class will take care of the Robot Tilt Widget Fucntions.  This
# Will Read from Serial in order to get gyroscopic information from the 
# robot.
###########################################################################
class Robot_Tilt():
    def __init__(self) -> None:
        self.canvas_size = (300, 300)
        pass

    def Generate_Frame(self, parentFrame, x, y) -> None:
        tilt_frame = tk.Frame(parentFrame, padx= 25, pady= 25)
        tilt_frame.grid(row= x, column= y)

        title= tk.Label(tilt_frame, text= "Robot Tilt Graphic")

        tilt_canvas = tk.Canvas(tilt_frame, bg= 'white', width= self.canvas_size[0], height= self.canvas_size[1])
        tilt_canvas.create_oval(self.canvas_size[0]/4, self.canvas_size[1], 3*self.canvas_size[0]/4, self.canvas_size[0]/2, fill= 'blue')
        
        title.grid(row= 0, column= 0)
        tilt_canvas.grid(row= 1, column= 0)
        

    def updatePosition() -> None:
        pass






###########################################################################
# The Below Class will take care of the PID Graphic,  it will show the 
# graphic POC/PID.png as well as show the PID magnitudes as sliders. These
# sliders will be user operable
###########################################################################
class PID():
    def __init__(self) -> None:
        self.p = 0
        self.i = 0
        self.d = 0

        self.P_LIMIT = (0, 100)
        self.I_LIMIT = (0, 100)
        self.D_LIMIT = (0, 100)


    def Generate_Frame(self, parent_frame, x, y) -> None:
        PID_frame = tk.Frame(master= parent_frame)
        PID_frame.grid(row= x,column= y, padx= 25, pady= 25)

        self.p_s = tk.IntVar(PID_frame, value= self.p)
        self.i_s = tk.IntVar(PID_frame, value= self.i)
        self.d_s = tk.IntVar(PID_frame, value= self.d)

        title = tk.Label(PID_frame, text= "PID Configurator")
        p_slider = tk.Scale(PID_frame, variable= self.p_s, length= 200, orient= 'horizontal', label= "Proportional Coefficient", from_= self.P_LIMIT[0], to= self.P_LIMIT[1])
        i_slider = tk.Scale(PID_frame, variable= self.i_s, length= 200, orient= 'horizontal', label= "Integral Coefficient", from_= self.I_LIMIT[0], to= self.I_LIMIT[1])
        d_slider = tk.Scale(PID_frame, variable= self.d_s, length= 200, orient= 'horizontal', label= "Derivative Coefficient", from_= self.D_LIMIT[0], to= self.I_LIMIT[1])

        apply_button = tk.Button(PID_frame, text= "Apply", command= lambda: self.applyPID)

        title.grid(row= 0, column= 0)
        p_slider.grid(row= 1, column=0)
        i_slider.grid(row= 2, column= 0)
        d_slider.grid(row= 3, column= 0)
        apply_button.grid(row=4, column= 0)

        
    def Apply_PID() -> None:
        pass


        



###########################################################################
# The below class will take care of the obstacle detection map.  This map 
# This map will grab pips everytime an obstacle is detected (with a LPF)
# and plot them on a canvas.
###########################################################################
class Obstacle_Detection_Map():
    def __init__(self) -> None:
        pass




if __name__ == "__main__":
    root = tk.Tk()
    root.title("SegWay Robot Client")
    mainframe = tk.Frame(master = root)
    mainframe.grid(row= 0, column= 0)
    my_PID = PID()
    my_tilt = Robot_Tilt()
    my_PID.Generate_Frame(mainframe, 0, 0)
    my_tilt.Generate_Frame(mainframe, 0, 1)

  

    


    root.mainloop()


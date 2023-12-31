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
        self.robot_wheel_radius = 75
        
        pass

    def Generate_Frame(self, parent_frame, x, y, rowspan, colspan) -> None:
        self.frame = tk.Frame(parent_frame, padx= 25, pady= 25)
        self.frame.grid(row= x, column= y, rowspan= rowspan, columnspan= colspan)
        title= tk.Label(self.frame, text= "Robot Tilt Graphic")
        self.canvas = tk.Canvas(self.frame, bg= 'white', width= self.canvas_size[0], height= self.canvas_size[1])

        self.Create_Wheel(self.robot_wheel_radius)
        self.Create_Vertical_Axis(self.robot_wheel_radius)
        self.Create_Azimuth(15, self.robot_wheel_radius, 400)
        # self.Create_Theta_Arc(15, self.robot_wheel_radius)
        
        title.grid(row= 0, column= 0)
        self.canvas.grid(row= 1, column= 0)
        
    def Create_Wheel(self, radius) -> None:
        self.robot_wheel = (self.canvas_size[0]/2-radius, self.canvas_size[1], self.canvas_size[0]/2+radius, self.canvas_size[1]-radius*2)
        self.canvas.create_oval(self.robot_wheel, fill= 'blue')

    def Create_Body(self, angle, width, height) -> None:
        pass

    def Create_Vertical_Axis(self, radius) -> None:
        self.canvas.create_line(self.canvas_size[0]/2, self.canvas_size[1] - radius, self.canvas_size[0]/2, 0, dash= 5, fill= 'black')
        pass

    def Create_Azimuth(self, angle, radius, length) -> None:

        angle = self.Degree_To_Radian(angle)
        
        x1 = self.canvas_size[0]/2
        y1 = self.canvas_size[1] - radius
        x2 = (int(np.sin(angle) * length) + self.canvas_size[0]/2)
        y2 = self.canvas_size[1] - radius - int(np.cos(angle) * length)

        self.canvas.create_line(x1, y1, x2, y2, dash = 5, fill= 'red')

        pass

    # def Create_Theta_Arc(self, angle, radius) -> None:
    #     angle = self.Degree_To_Radian(angle)

        
    #     length = self.canvas_size[1] - radius * 3/4

    #     x1 = self.canvas_size[0]/2
    #     y1 = self.canvas_size[1]
    #     x2 = (int(np.sin(angle) * length) + self.canvas_size[0]/2)
    #     y2 = self.canvas_size[1] - radius - int(np.cos(angle) * length)

    #     self.canvas.create_arc(x1, y1, x2, y2, style= tk.ARC)



    def Degree_To_Radian(self, angle) -> float:
        return angle * (np.pi / 180)

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


    def Generate_Frame(self, parent_frame, x, y, rowspan, colspan) -> None:
        PID_frame = tk.Frame(master= parent_frame)
        PID_frame.grid(row= x,column= y, rowspan= rowspan, columnspan= colspan, padx= 25, pady= 25)

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
    
    def Generate_Frame(self, parent_frame, x, y) -> None:
        pass

    def resize(self) -> None:
        pass
    
    def create_pip(self) -> None:
        pass

    def create_robot(self) -> None:
        pass



###########################################################################
# The below class will create a widget that shows the previous ten seconds
# of angular displacement, this angular displacement will allow calculation
# of Overshoot, settling time, damping factor, etc.
###########################################################################
class Damping_Features():
    def __init__(self) -> None:
        self.settling_time = 0
        self.overshoot = 0
        self.rise_time = 0
        self.damping_ratio = 0
        self.peaking_time = 0
        pass

    def Generate_Frame(self,parent_frame, x, y, rowspan, colspan) -> None:
        self.frame = tk.Frame(parent_frame, padx= 25, pady= 25)
        self.frame.grid(row= x, column= y, rowspan= rowspan, columnspan= colspan)
        title= tk.Label(self.frame, text= "Damping Features")
        
        title.grid(row= 0, column= 0, rowspan= 10)

        self.settling_time_label = tk.Label(self.frame, text = f"Settling Time: {self.settling_time}")
        self.overshoot_label = tk.Label(self.frame, text = f"Overshoot: {self.overshoot}")
        self.rise_time_label = tk.Label(self.frame, text = f"Rise Time: {self.rise_time}")
        self.damping_ratio_label = tk.Label(self.frame, text = f"Damping Ratio: {self.damping_ratio}")
        self.peaking__time_label = tk.Label(self.frame, text = f"Peaking Time: {self.peaking_time}")


        self.damping_ratio_label.grid(row= 2, column=0)
        self.overshoot_label.grid(row= 2, column= 1)
        self.rise_time_label.grid(row= 2, column= 2)
        self.peaking__time_label.grid(row= 2, column= 3)
        self.settling_time_label.grid(row=2, column= 4)


    def Get_Reference_Signal(self) -> float:
        pass

    def Get_Actual_Signal(self) -> float:
        pass

    def Get_Error_Signal(self) -> float:
        pass

class Aprroximate_System_Model():
    def __init__(self) -> None:
        pass

    def generate_frame(self, parent_frame, x, y, rowspan, colspan):
        pass

    def feed_forward() -> None:
        pass



if __name__ == "__main__":

    root = tk.Tk()
    root.title("SegWay Robot Client")
    mainframe = tk.Frame(master = root)
    mainframe.grid(row= 0, column= 0)
    my_PID = PID()
    my_tilt = Robot_Tilt()
    my_damping = Damping_Features()
    my_PID.Generate_Frame(mainframe, 0, 0, rowspan= 1, colspan= 1)
    my_tilt.Generate_Frame(mainframe, 0, 1, rowspan= 1, colspan= 1)
    my_damping.Generate_Frame(mainframe, 1, 0, rowspan= 2, colspan= 1)

  

    


    root.mainloop()


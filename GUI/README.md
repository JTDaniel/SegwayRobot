# Client GUI

The purpose of this GUI is to allow the robot operater to have an informational interface for all feedback and systems in the Segway robot control system.  This will allow the user to see:
<ul>
Robot Tilt
PID Sliders/Feedback
Obstacle Detection Map
Which Sensors are attached
Battery Voltage
</ul>

## Robot Tilt
The Robot Tilt Widget will show a live graphic of the robot, this robot graphic is a profile view of the segway, showing the robot tilt as it corresponds to the gyroscopic sensor data.

## PID Sliders/Feedback
The PID Sliders will show a PID Graphic will show   
<img src="../Planning/PID.png>

This graphic will have PID Sliders that allow the operater to adjust sliders and see how a system may: become unstable, respond to high frequency dynamics, not follow low frequency disturbance, etc.

## Obstacle Detection Map
The Obstacle Detection map will show a canvas, this canvas will be populated by "pips" as the robots ranging sensors detect obstacles.  Given time, the canvas will be populated with enough pips to show a map of obstacles.

## Sensors Attached
This List will show which sensors are attached and their I2C addresses

## Battery Voltage
This label will show the battery voltage reading onboard the robot.
# ROS part #

## Introduction:

In this part you will learn how to connect to the robot by ssh, download the package into the src file and run the code you want in the robot by using ROS.

### Requirement:

* Some basics in ROS (how to launch files and the basic commands).
* Some basics in Python to understand how the Niryo package works, be able to modify it and to create your own code.
* Ubuntu basic commands. 

## Software environment :

Niryo One is compatible with ROS Kinetic, it doesn’t support melodic version like his new brother Ned. There’s already a ROS Kinetic version installed in the raspberry Pi of the robot. You don’t have to install nothing. There’s also all the package and the files to run python, you have just to reach the Raspberry Pi by ssh. 

## SSH connection:
SSH connection allow you to access to the Raspberry Pi in order to run some files, add, modify …etc. We need to pass by this method to handle the robot and execute some codes using ROS with or without using Python. Because ROS can run C++ files also. 

***Ensure that your computer is connected to the robot wi-fi network***

* If you have windows, you can download Putty and then connect by SSH, that will allow you to have a visual interface of the Raspberry Pi. Or, you can just tap the SSH command in the command Prompt, to do that you can follow this video [here](https://www.youtube.com/watch?v=UPXnop3C6JQ&ab_channel=ITProTV) 

* For Linux, you can just type this command : (the IP address for Niryo by default is 10.10.10.10)

```bash
ssh niryo@10.10.10.10
```
Password by default is robotics

***If there's no SSH server in your device you can install it by following this procedure :***

1.	Open the terminal application for Ubuntu desktop.
2.	Type:

```bash
sudo apt-get install openssh-server
```

4.	Enable the ssh service by typing:  
```bash
sudo systemctl enable ssh
```
5.	Start the ssh service by typing: 
```bash
sudo systemctl start ssh
``` 
6.	Test it by login into the system using:
```bash
ssh niryo@10.10.10.10
``` 

## Use ROS ## 

Now you are connected to the robot by SSH and ready to start. In the Raspberry Pi you will find all the packages of ROS for using Niryo. Run this command to enter to ROS workspace :
```bash
cd catkin_ws/src/
```
Here there are all the ROS packages that you can use. You can start by tapping this command 
```bash
Rosrun niryo_one_python_api basic_api_functions
```
The robot will start by calibrate itself and then execute the order. In all the files there’s a condition, which allows the robot to check if it’s already calibrated or not and make the calibration if it’s not the case.

## Python API Niryo ##

You can find this package in this folder <br/>
\catkin_ws\src\niryo_one_ros\niryo_one_python_api\ <br/>
There are some examples of code to execute and maybe understand what they can do and how. Theses examples are the same as the code that you will downloaded from here. It uses the API Python library to control the robot. This library has a lot of functions that use ROS so you can just have some basics in python and you can be able to use this library and control the robot.  <br/>
The main file containing all the functions is located here <br/>
\catkin_ws\src\niryo_one_ros\niryo_one_python_api\src\niryo_one_python_api <br/>
To know more about each function and how to use it, visit this [website](https://github.com/NiryoRobotics/niryo_one_ros/tree/master/niryo_one_python_api)

## Download Niryo_One_pkg and run codes ##

ROS package contains 3 principals files: CMakeLists.txt, package.xml, these two files are created automatically while creating a package. and the third file is a python or cpp file where the code must be written. The package in this github repository has CMakeLists.txt, package.xml and three python files in the scripts folder. To use these files as a ROS package, you have to download it in catkin_ws/src/ folder. To do it follow these steps:
 ```bash
cd catkin_ws/src/
git clone https://github.com/zainbinsumait/Niryo-One-Project/tree/main/Niryo_One_ROS_Pkg

```
and Then type this command to make ROS recognize the package :
```bash
cd ..
catkin_make
cd src
source devel/setup.bash
```
Then you can run this file as an example after making sure that all the environment is ready :

```bash
rosrun Niryo_One_ROS_Pkg pick_test.py
```

This will make the robot pick one piece from the workspace 2 (manually made workspace) to the workspace 1. 

## Code explanations:

In the package, the three codes are:<br/>
* pick_test_without_conveyer.py:<br/>
This code causes the robot to go to the observation position linked to the new_workspace.  Change the name to match the name of your workspace 2 (Line 35).  Then the robot tries to detect a red square object (you can change these parameters in line 55).<br/>
If it detects the object, it will take it and place it in the other workspace called "robotics_workspace" (this name should also be changed in line 69).  And it ends up returning to his initial position and closing the gripper.<br/>
Ps: In the code, there are detailed comments.

* pick_green_circle_with_conveyer.py:<br/>
This code does the same as the first one except that it also uses the conveyor and the IR sensor.  So, the sensor detects the object, the conveyor stops after 3 seconds and the robot will pick up the object if it was a green circle (you can change this too). Then drop it in the other workspace and return to its initial state.

* pick_n_sort_by_color_with_conveyer.py:<br/>
This code is an update of the previous code.  It detects all types of objects and classifies them according to their colors. It repeats this 5 times.  You can change the number of repetitions as well as the position where to place each color.<br/>



## Troubleshooting ##

<br/>
When you use ROS, sometimes the code does not work.  This problem arises from the initialization of the parameters.  To avoid that, you can run the code (pick_n_place_with_conveyer) to put the robot into learning mode, and press ctrl + c to quit the program.<br/>
You can also use this code to create a new workspace using ROS.  It asks you to position the robot in the landmarks, one after the other.  Then it turns on the conveyor and when it sees an object.  It stops the conveyor and takes the object (it must be red square) then it comes to put the object back in the same workspace.<br/>

 To start this program, type this command:
```bash
rosrun niryo_one_python_api pick_n_place_with_conveyer.py
```

* 


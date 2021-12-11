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
 



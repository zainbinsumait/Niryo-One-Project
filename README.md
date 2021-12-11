# Niryo-One-Project #

#### Projet Niryo One (ESIREM 4A program) ####

## Outlines: ##
1. Introducion 
2. What’s is Niryo ?
3. Environment setup
4. How to turn on the robot and connect to your laptop
5. Power off the robot
6. Troubleshooting



## Introduction : 

This project had been done during my engineering program ROBOTICS AND INSTRUMENTATION at ESIREM  (school of materials research and engineering) at Le Creusot campus - France. 

#### Objectives: 

The project involves exploring Niryo One 6-axis collaborative robot arm 

Then in a first part learn how to handle it by its already built software and in a second part manipulate it by ROS. In the end, write a code by both ways to make the robot pick some pieces and place them in depending in every piece color.


 

## What is Niryo ?

The French-made 6-axis collaborative robot is intended for: <br/>
* Higher education
* Vocational training
* R&D laboratories
* small businesses.<br/>

This robotic arm is made using 3D printing, which opens up a lot of possibilities, such as making your own 3D printed tools, developing applications, connecting with a community involved in this open-source project, and even accessing a whole library of codes to customize the robotic arm to your needs and use.
<br/><br/><br/>
There are now two versions of Niryo :
* Niryo One.
* Niryo Ned.

In this project we explore just Niryo One. If you have Niryo ned you can go to click [here](https://docs.niryo.com/product/ned/v3.2.0/en/source/introduction.html)
<br/><br/><br/>
For all the mechanical specifications, check the pdf included which contains :
* Niryo One
    * 6 axis overview
    * Dimensions
    * Max rotation per axis
    * Integration
* Tools
    * Specs and dimensions for 5 tools
    * Integration

For all Niryo One Documentaions you can visit their official website [here](https://niryo.com/docs/niryo-one/). 
<br/>
#### Two ways to program and manipulate the robot : 

**By using Niryo One Studio :**
This software is developed by the community to make this robot accessible to students and beginners. It uses Scratch language to create some code and run it in the robot. It’s very easy to use and provide all the function that you can use to do whatever you want. To now more about this software [click here](https://github.com/zainbinsumait/Niryo-One-Project/blob/main/Niryo%20One%20Studio/README.md)

**By using ROS:**
The Robot Operating System ( [ROS](https://www.ros.org/)).  is a set of software libraries and tools that help you build robot applications. here we will not involve ROS courses, which many other websites do it well, we will just explain how to use the Niryo library in ROS, and how to run it in the robot. This will be in the second part.


## Environment setup:
In order to manipulate the robot and use the vision function, we prepare this environment. 

We have:
* Niryo One Robot.
* Vision set (which can be bought with the robot):
A complete vision set and a manually built workspace that we print it let call it (WS2), you can find the 3D module in the files.<br/>
![vision set](https://user-images.githubusercontent.com/76461363/145681430-627d3eca-525a-42ed-9af9-7a32679f2b0a.PNG)

<img src="https://user-images.githubusercontent.com/76461363/145681029-42783b11-92fe-4fdc-885c-1c2395b309fb.jpg" width="300" height="400" />


* Convoyer built (which can be also bought with the robot):
This built is used to translate the pieces to the WS2, and simulate a production line of a company.<br/>
![convoyer](https://user-images.githubusercontent.com/76461363/145681428-b4970899-bdc1-4d91-af78-405bf7feeb48.PNG)


<img src="https://user-images.githubusercontent.com/76461363/145681042-bfffe9a8-555e-49b2-b7b9-4e162e037542.jpg" width="600" height="400" />

*  IR sensor to detect the presence of an object.<br/>
<img src="https://user-images.githubusercontent.com/76461363/145681054-7787e665-b5ed-481d-bdbd-69f43233892f.jpg" width="600" height="400" />

<br/>



***Ensure that the robot is stable on a flate table to avoid it's fall***<br/>
***Now we are ready to start and learn more about the input/output of the robot


## Turn on the robot and connect to your laptop

<br/>

![backside](https://user-images.githubusercontent.com/76461363/145484486-83e72050-7a91-4256-b6bc-1c54b14d9247.PNG "Backside")

#### In order to know how to deal with the robot, it's necessary to know this buttons and I/O :

1. Top button.
2. Ethernet port of the Raspberry Pi 3B.
3. USB port * 4.
4. LED.
5. CAN bus connection for Niryo Steppers * 2. Not used yet.
6. Dynamixel XL-320 connector. Used for the vacuum pump.
7. Dynamixel XL-430 connector. Not used yet.
8. 12 V switch output * 2. Actionable through software.
9. GPIO panel * 2. Total 6 digital pins, actionable through software. You can use GPIO1 and GPIO2 pins as 5V digital pins (mode: input or output, state: high or low).
10. Power switch. 
11. Power adapter connector.<br/>



#### Steps to turn on the robot :
* Connect the robot to a the original Power Supply (11),connect also the built if you want to use it.
***Ensure your power adapter has an 11.1V output and is able to provide 6A. Lower output
voltage and current may cause the robot to fail to move correctly. Higher output voltage and
current may permanently damage the robot, and can be a cause of fire.***
.<br/>
* Turn on the robot by the power switch . (The LED (4) will turn into red color).<br/>
![Capture](https://user-images.githubusercontent.com/76461363/145487841-f7059567-52c6-4de5-a4de-7292211f7220.PNG)


* Wait until the LED becomes blue or green to be able to use the robot. <br/>
![2](https://user-images.githubusercontent.com/76461363/145487833-18ed7a3e-9d85-4564-b546-11e01ab0ce62.PNG)

* While the LED is blue, The robot will create its own Wi-Fi network. You can find it on your computer Wi-Fi manager. The name of the Wi-Fi network starts with “Niryo_One” followed by a series of numbers and letters, which makes a unique identifier linked to the Raspberry Pi 3B serial number. Network password is "niryone" by default
* If you want to use the convoyer built and the IR sensor, you have to connect them to the robot like this (in the left IR sensor and the convoyer built in the right) : <br/>
<img src="https://user-images.githubusercontent.com/76461363/145681047-5c13443d-5d9f-496c-b78f-74a54b5eda5b.jpg" width="600" height="400" />
* Once connected, you can now start handling the robot by One of the ways that we mentionned.<br/>


***[click here](https://github.com/zainbinsumait/Niryo-One-Project/blob/main/Niryo%20One%20Studio/README.md) for Niryo One software***

<br/>

***[click here](https://github.com/zainbinsumait/Niryo-One-Project/tree/main/ROS%20part/Niryo_One_Pkg) for ROS***




## Power off the robot 
To turn off the robot, press the top button for 3 secondes until the LED becomes purple then wait a moment until it becomes red then you can turn off by the power switch.


## Troubleshooting ##

Normaly until now you will not have any problems, 



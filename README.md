# Niryo-One-Project #

#### Projet Niryo One (ESIREM 4A program) ####


## Introduction : 

This project had been done during my engineering program at ESIREM ( school of materials research and engineering ) at Le Creusot campus - France. 

### Objectives: 

The project involves exploring Niryo One 6-axis collaborative robot arm 

Then in a first part know how to handle it by its already built software and in a second part manipulate it by ROS.


## Exploring the robot: 

Niryo One robot is a collaborative and open source 6-axis robot created by Niryo society society in france for: 

* Higher education 

* Vocational training 

* R&D laboratories 

Its use is particularly adapted to study robotics and programming in the context of the industry 4.0.





## User guide 

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


#### Software requirement :
* Download the software from this web site https://niryo.com/download/

#### Steps to start using the Robot with the software Niryo One Studio:
* Connect the robot to a the original Power Supply (11),connect also the built if you want to use it.
* Turn on the robot by the power switch . (The LED (4) will turn into red color).<br/>
![Capture](https://user-images.githubusercontent.com/76461363/145487841-f7059567-52c6-4de5-a4de-7292211f7220.PNG)


* Wait until the LED becomes blue or green to be able to use the robot. <br/>
![2](https://user-images.githubusercontent.com/76461363/145487833-18ed7a3e-9d85-4564-b546-11e01ab0ce62.PNG)

* While the LED is blue, The robot will create its own Wi-Fi network. You can find it on your computer Wi-Fi manager. The name of the Wi-Fi network starts with “Niryo_One” followed by a series of numbers and letters, which makes a unique identifier linked to the Raspberry Pi 3B serial number. Network password is "niryone" by default
* Once connected, you can now lauch the executable file (NiryoOneStudio) in the folder downloaded. Normally it will be in the sub-folder specifyng the number of bits of your computer.

```bash
cd Desktop/NiryoOneStudio-linux-x64/
./NiryoOneStudio
```
Overview <br/> <br/>

![4](https://user-images.githubusercontent.com/76461363/145490882-a907e2a8-97af-429b-b28a-c505c1289f08.PNG)


* Once the software launched,on the right of the toolbar, you can see the current connection state: “Connected to” + IP
address, or “Not connected”. Connect to the niryo. Just press the button **Connect to Niryo One**. <br/> <br/>
![3](https://user-images.githubusercontent.com/76461363/145489367-50daf4a6-e8ba-4828-9703-54a128950074.PNG)

* Calibration : After the robot has been successfully launched (LED green or blue), and before you can give a
move command to the robot, you will need to calibrate it. Also, if a Niryo Stepper motor was
disconnected and reconnected, a calibration will be required. Chose **auto calibration**.
* after a succes calibration, the robot mow is ready.

#### Menu  <br/> <br/>
![5](https://user-images.githubusercontent.com/76461363/145490932-dbeddba9-d75c-4457-bb79-e8ff08263183.PNG)


#### State section and learning mode <br/> <br/>
![7](https://user-images.githubusercontent.com/76461363/145493261-e4b2af38-b29c-4c06-becb-07b6b59f9e69.PNG)

1. 3D view of the robot.<br/>
**The 3D view can help you see if a manual or auto calibration was not done correctly. If
there is an offset between what you see on the screen and your robot (ex: the axis 1 is clearly
not at the same position), then you should probably do the auto-calibration again.**
2. “Learning mode” button. <br/>
**Activating the learning mode will deactivate the torque on all
motors. When the robot is in “learning mode”, you can move it with your hand. When the
“learning mode” is off, the torque is activated on all motors and you can’t move the robot with
your hand.
When the robot is powered on and you don’t use it, it’s better to let it in “learning mode”.
This will avoid heat and motor problems on the long run.**
3. “Stop” button. At any time, click on this button to stop the current robot trajectory.
4. Current joints state (1-6).
5. Current TCP (Tool Center Point) position and orientation.
6. “Save current position” button. You can save the current position and give it a name, so you
can reuse it later.
7. Current arm max speed. You can modify it at any time (0-100%).
8. Current selected tool.



#### launch a scratch code <br/>
To launch an existing code:
* go to the Niryo blocks panel in the left menu.<br/> <br/>
![6](https://user-images.githubusercontent.com/76461363/145491338-f7ed2042-0932-4537-b12d-3fb3479df95d.PNG)

  1. This is the workspace. Your whole program will be there.
  2. Clicking on this icon will center the workspace on your blocks.
  3. Workspace zoom control.
  4. To delete a block, simply drag it and drop it onto the trash. You can also select it and press
  the delete key on your keyboard.
  5. Clear the current workspace.
  6. Undo/Redo. You can also use CTRL + Z, and CTRL + MAJ + Z
  7. Add a position block.
  8. Play the sequence displayed on the workspace. Once the sequence is done (success or not),
  you’ll get a notification on the bottom of the screen.
  9.  Stop the current sequence execution.
  10.   Import / Export Blocks.
  11.   The “Niryo One” functions.

* chose the button number 10 and then chose **Import Blocks from your computer (XML)**.
* Then chose your file and press **Open** (Sorting file holding the name "pick_n _sort_depending_on_color")<br/>
***Important: this code uses the built and the presence sensor so make sure they are connected in this way (the built in the stepper output in the left-up and the presence sensor in the right GPIO1):***
<br/><br/>
![20211126_110719](https://user-images.githubusercontent.com/76461363/145494286-244e590f-7e59-4efc-8fc4-f8a213331d92.jpg)<br/>
***make sure also that the markers in the workspace are clear to see by the robot camera***<br/><br/>
![20211126_110644](https://user-images.githubusercontent.com/76461363/145494882-4ba2ad5e-1951-4123-82b7-40cf7142fd5b.jpg)


* Run the code by pressing the button play (8).<br/>

***If there's a problem, ensure that the robot choose well the large gripper. Go to robot command panel in the left menu -> tool command: choose large gripper then press SELECT***

***In the end of this code the shapes will be sorted like this :***<br/><br/>
![20211126_102141](https://user-images.githubusercontent.com/76461363/145495045-d8dd46ea-89c4-421e-bb1c-1ae63bb0212a.jpg)



#### Power off the robot 
To turn off the robot, press the top button for 3 secondes until the LED becomes purple then wait a moment to let the LED becomes red then you can turn off by the power switch.







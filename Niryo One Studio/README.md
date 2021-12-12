# Niryo One Studio Software #

In this part, we will learn how to use Niryo One Studio Software and how to run the files XML. Start by downloading all the files in this repository and follow the steps bellow. The robot is supposed to be already turned on and the laptop is connected to the robot network hotspot.


## Software requirement :
* Download the software from this [web site](https://niryo.com/download/)

## Steps to start using the Robot with the software Niryo One Studio:

you can now lauch the executable file (NiryoOneStudio) in the folder downloaded. Normally it will be in the sub-folder specifyng the number of bits of your computer.

If you use Linux_x64 device you can run this command : <br/>
```bash
cd NiryoOneStudio-linux-x64/
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
2.  Clicking on this icon will center the workspace on your blocks.
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
<img src="https://user-images.githubusercontent.com/76461363/145494286-244e590f-7e59-4efc-8fc4-f8a213331d92.jpg" width="600" height="400" /><br/>
***make sure also that the markers in the workspace are clear to see by the robot camera***<br/><br/>
<img src="https://user-images.githubusercontent.com/76461363/145494882-4ba2ad5e-1951-4123-82b7-40cf7142fd5b.jpg" width="600" height="400" /><br/>



* Run the code by pressing the button play (8).<br/>

***If there's a problem, ensure that the robot choose well the large gripper. Go to robot command panel in the left menu -> tool command: choose large gripper then press SELECT***

***In the end of this code the shapes will be sorted like this :***<br/><br/>
<img src="https://user-images.githubusercontent.com/76461363/145495045-d8dd46ea-89c4-421e-bb1c-1ae63bb0212a.jpg" width="300" height="450" /><br/>


## Codes description ##

Four files XML which can be executed by using the software:
* pick_test.xml :<br/>
This code will just make a test to see if your robot can pick pieces or not. It will use neither the conveyor built nor the IR sensor.
***Ensure that you modified the workspace name in the code, choose a workspace that you had already registered<br/>
This code doesn't choose the large gripper automatically so ensure that you have selected it in robot command panel from the left menu -> tool command: choose large gripper then press SELECT***
* pick_from_WS_to_convoyer.xml:<br/>
This one will pick an object from the workspace 1 to the conveyer. It will run neither the conveyor built nor the IR sensor.
* pick_test_with_convoyer_ws.xml :<br/>
It will start by turn on the built and then if IR sensor detects an object, it will pick it and put it in the workspace 1. It needs all the environment setup, and you must place the workspace to close to the robot so it can see the four markers.
* pick_n _sort_depending_on_color.xml :<br/>
This is the finale version of the code, it picks up the object, which had been detected by the IR sensor. Then according to its color, it will place it in each of the corners of  WS1 (workspace 1).



## Power off the robot 
To turn off the robot, press the top button for 3 secondes until the LED becomes purple then wait a moment until it becomes red then you can turn off by the power switch.

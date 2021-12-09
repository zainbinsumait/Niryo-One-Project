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

* Once the software launched,on the right of the toolbar, you can see the current connection state: “Connected to” + IP
address, or “Not connected”. Connect to the niryo. Just press the button **Connect to Niryo One**. <br/> <br/>
![3](https://user-images.githubusercontent.com/76461363/145489367-50daf4a6-e8ba-4828-9703-54a128950074.PNG)

* Calibration : After the robot has been successfully launched (LED green or blue), and before you can give a
move command to the robot, you will need to calibrate it. Also, if a Niryo Stepper motor was
disconnected and reconnected, a calibration will be required.







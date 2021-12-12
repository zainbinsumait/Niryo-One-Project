#!/usr/bin/env python

# To use the API, copy these 4 lines on each Python file you create
from niryo_one_python_api.niryo_one_api import *
import math
import rospy
import numpy as np
import time
import cv2


rospy.init_node('niryo_one_project_test3')

print "--- Start"

n = NiryoOne()

try:
    # Calibrate robot first
    n.calibrate_auto()
    print "Calibration finished !"

    # the number of repetition 
    a = 0
    while a < 5 :

        # memorise the initate position
        pos_initi = n.get_arm_pose()

        #desable learning mode

        n.activate_learning_mode(False)

        #take the observation position
        observation_pose = n.get_target_pose_from_rel("new_workspace", 0.3, 0.3, 0.8, 0)
        observation_pose = n.robot_state_msg_to_list(observation_pose)

        # Conveyor
        conveyor_id = CONVEYOR_ID_ONE
        n.set_conveyor(CONVEYOR_ID_ONE, True)
        n.control_conveyor(conveyor_id, True, 100, CONVEYOR_DIRECTION_BACKWARD)

        #check the presence of the object
        object_pr = n.digital_read(GPIO_1A)

        time_start = rospy.get_time()

        while object_pr:
            object_pr = n.digital_read(GPIO_1A)

            time = rospy.get_time()
            print time
                #wait 20 seconds for the object, if not close the program
            if time == time_start + 20 :
                print "time out"
                exit()

        print("we have an object !!")

        #wait 3 seconds for the object to be in the center of the workspace
        n.wait(3)
        #stop convoyer
        n.control_conveyor(conveyor_id, True, 0, CONVEYOR_DIRECTION_BACKWARD)

        # Wait conveyor speed=0
        conveyor_id, connection_state, running, speed, direction = n.get_conveyor_1_feedback()
        while not speed == 0:
            n.wait(0.1)
            conveyor_id, connection_state, running, speed, direction = n.get_conveyor_1_feedback()


        #change tool to gripper
        n.change_tool(TOOL_GRIPPER_2_ID)

        print "i'll pick it"

        #go to observation position
        n.move_pose(*observation_pose)

        #initialise the parameters of finding an object
        objectred_found = False #the statu of finding a red object
        objectblue_found = False
        objectgreen_found = False


        # Wait object
        while not objectred_found and not  objectblue_found and not objectgreen_found :
            n.wait(0.1)
            #searching about blue, green or red object 
            #it doesn't work with me when i use both of COLOR_ANY and SHAPE_ANY together
            #so i had to seperate them
            objectblue_found, rel_pose, obj_shape, blue_color = n.detect_object("new_workspace", SHAPE_ANY , COLOR_BLUE )
            ShapeB = obj_shape
            objectgreen_found, rel_pose, obj_shape, green_color = n.detect_object("new_workspace", SHAPE_ANY , COLOR_GREEN )
            ShapeG = obj_shape
            objectred_found, rel_pose, obj_shape, red_color = n.detect_object("new_workspace", SHAPE_ANY , COLOR_RED)
            ShapeR = obj_shape


        # Pick the object and do a color sort

        #color red 
        if red_color == "RED" :
            
            print "Object seen  : color = " +  red_color  + " shape = " + ShapeR

            n.vision_pick("new_workspace", 0.0025, SHAPE_ANY, COLOR_RED)

            #Place
            place_pose = n.get_target_pose_from_rel("robotics_workspace", 0.034, 0.1, 0.5, 60)
            place_pose_raw = n.robot_state_msg_to_list(place_pose)
            n.place_from_pose(*place_pose_raw)

        elif green_color == "GREEN" :

            print "Object seen  : color = " +  green_color  + " shape = " + ShapeG

            n.vision_pick("new_workspace", 0.0025, SHAPE_ANY, COLOR_GREEN)

            #Place
            place_pose = n.get_target_pose_from_rel("robotics_workspace", 0.034, 0.9, 0.9, 0)
            place_pose_raw = n.robot_state_msg_to_list(place_pose)
            n.place_from_pose(*place_pose_raw)

        elif blue_color == "BLUE" :

            print "Object seen  : color = " +  blue_color  + " shape = " + ShapeB

            n.vision_pick("new_workspace", 0.0025, SHAPE_ANY, COLOR_BLUE)

            #Place
            place_pose = n.get_target_pose_from_rel("robotics_workspace", 0.034, 0.9, 0.1, 0)
            place_pose_raw = n.robot_state_msg_to_list(place_pose)
            n.place_from_pose(*place_pose_raw)

        else :
            print "there is no object ?!"

        #move to the initial position
        pose_I = n.robot_state_msg_to_list(pos_initi)
        n.move_pose(*pose_I)

        #close the gripper
        n.close_gripper(TOOL_GRIPPER_2_ID,300)
        #increase the number of repition by one
        a = a + 1

        #activate learning mode and change the tool
        n.activate_learning_mode(True)
        n.change_tool(TOOL_NONE)
    # exit the program
    exit()

except NiryoOneException as e:
    print e
    # handle exception here
    # you can also make a try/except for each command separately

print "--- End"



#!/usr/bin/env python

# To use the API, copy these 4 lines on each Python file you create
from niryo_one_python_api.niryo_one_api import *
import math
import rospy
import numpy as np
import time
import cv2


rospy.init_node('niryo_one_project_test')

print "--- Start"

n = NiryoOne()

try:
    # Calibrate robot first
    n.calibrate_auto()
    print "Calibration finished !"

    # memorise the initate position
    pos_initi = n.get_arm_pose()

    #desable learning mode
    n.activate_learning_mode(False)

    #Go to the observation position of the workspace "new_workspace"
    observation_pose = n.get_target_pose_from_rel("new_workspace", 0.3, 0.3, 0.8, 0)
    #get_target_pose_from_rel(workspace, height_offset from the workspace, x_rel, y_rel, yaw_rel)
    # (0,0) correspond to the different landmark corner of the workspace
    #workspace relative pose: X_REL (in [0,1]), Y_REL (in [0,1]), YAW_REL (in [-π,π])
    
    observation_pose = n.robot_state_msg_to_list(observation_pose)
    #this function convert object of robot_state_msg type to list
    #this is the robot_stat_msg, it has position xyz and rpy with angles 
    #position: x: (float) y: (float) z: (float)
    #rpy: roll: (float) pitch: (float) yaw: (float)

    # Conveyor
    conveyor_id = CONVEYOR_ID_ONE
    n.set_conveyor(CONVEYOR_ID_ONE, True)
    n.control_conveyor(conveyor_id, True, 100, CONVEYOR_DIRECTION_BACKWARD)

    #check the presence of the object
    object_pr = n.digital_read(GPIO_1A)

    while object_pr:
        object_pr = n.digital_read(GPIO_1A)

    print("we have an object !!")

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
    n.move_pose(*observation_pose)

    object_found = False
    # Wait object
    # Wait for green circle object (you can put RED or BLUE instead of GREEN and SQUARE instead of CIRCLE)
    
    while not object_found:
        n.wait(0.1)
        object_found, rel_pose, obj_shape, obj_color = n.detect_object("new_workspace", SHAPE_CIRCLE, COLOR_GREEN)

    print "Object seen"

    # Pick the green round object
    #vision_pick(workspace, height_offset, shape, color)
        #Parameters:
        #name of the workspace: WORKSPACE_NAME
        #height offset for picking: HEIGHT_OFFSET expressed in m
        #object shape to detect: SHAPE must be one of: Shape Enum
        #object color to detect: COLOR must be one of: Color Enum
    n.vision_pick("new_workspace", 0.0025, SHAPE_CIRCLE, COLOR_GREEN)

    #Place
    place_pose = n.get_target_pose_from_rel("robotics_workspace", 0.07, 0.5, 0.5, 0.45)
    place_pose_raw = n.robot_state_msg_to_list(place_pose)
    n.place_from_pose(*place_pose_raw)

    #return to the initial position 
    pose_I = n.robot_state_msg_to_list(pos_initi)
    n.move_pose(*pose_I)
    
    #close the gripper with a speed of 300
    n.close_gripper(TOOL_GRIPPER_2_ID,300)

    #activate learning mode and change the tool
    n.activate_learning_mode(True)
    n.change_tool(TOOL_NONE)
    exit()

except NiryoOneException as e:
    print e
    # handle exception here
    # you can also make a try/except for each command separately

print "--- End"



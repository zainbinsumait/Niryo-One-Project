#!/usr/bin/env python

# To use the API, copy these 4 lines on each Python file you create
from niryo_one_python_api.niryo_one_api import *
import math
import rospy
import numpy as np
import time
import cv2


rospy.init_node('niryo_one_project')

print "--- Start"

def f(compressed_image):
    np_arr = np.fromstring(compressed_image, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    return img

n = NiryoOne()

try:
    # Calibrate robot first
    n.calibrate_auto()
    print "Calibration finished !"

    pos_initi = n.get_arm_pose()
    n.activate_learning_mode(False)

    print "Go to observation position"
    observation_pose = n.get_target_pose_from_rel("new_workspace", 0.3, 0.3, 0.8, 0)
    observation_pose = n.robot_state_msg_to_list(observation_pose)
    #raw_input("Marker  (Press enter when the robot is correctly positioned")
    n.change_tool(TOOL_GRIPPER_2_ID)
    img = n.get_compressed_image()
    img = f(img)

    filename = 'savedImage.jpg'
    cv2.imwrite(filename, img)

    object_found = False
    # Wait object
    while not object_found:
        n.wait(0.1)
        object_found, rel_pose, obj_shape, obj_color = n.detect_object("new_workspace", SHAPE_SQUARE, COLOR_RED)

    print "Object seen"

    # Pick
    n.vision_pick("new_workspace", 0.0025, SHAPE_SQUARE, COLOR_RED)

    #Place
    place_pose = n.get_target_pose_from_rel("robotics_workspace", 0.0025, 0.5, 0.5, 0.45)
    place_pose_raw = n.robot_state_msg_to_list(place_pose)
    n.place_from_pose(*place_pose_raw)
    
    pose_I = n.robot_state_msg_to_list(pos_initi)
    n.move_pose(*pose_I)

    n.close_gripper(TOOL_GRIPPER_2_ID,300)

    n.activate_learning_mode(True)
    rospy.spin()
except NiryoOneException as e:
    print e
    # handle exception here
    # you can also make a try/except for each command separately

print "--- End"
 



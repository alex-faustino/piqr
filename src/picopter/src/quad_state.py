#!/usr/bin/env python

import rospy
import numpy as np
from geometry_msgs.msg import Pose
from pyquaternion import Quaternion


def poseCb(tag_pose):
	# Put ROS messages in to numpy arrays and quaternions
	q_tag_in_cam = Quaternion(tag_pose.orientation.w,
							  tag_pose.orientation.x,
							  tag_pose.orientation.y,
							  tag_pose.orientation.z)
							  
	o_tag_in_cam = np.array([tag_pose.position.x,
							 tag_pose.position.y,
							 tag_pose.position.z])
							
	# Convert quaternion in to rotation matrix
	# then use it to find inverse position and orientation
	rot_tag_in_cam = q_tag_in_cam.rotation_matrix
	rot_cam_in_tag = rot_tag_in_cam.transpose()
	o_cam_in_tag = -rot_cam_in_tag.dot(o_tag_in_cam)
	q_cam_in_tag = Quaternion(matrix=rot_cam_in_tag)
	
	print o_cam_in_tag
	print q_cam_in_tag
	
def getRawData():
	# Initialize node
	rospy.init_node('quad_state', anonymous=True)
	
	# Subscribe to AprilTag publisher
	rospy.Subscriber("tag_detector/tag_pose", Pose, poseCb)
	
	rospy.spin()
	
if __name__ == '__main__':
	getRawData()

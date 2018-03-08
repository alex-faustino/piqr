#!/usr/bin/env python

import rospy
import numpy as np
import time
from geometry_msgs.msg import Pose
from pyquaternion import Quaternion
from picopter.msg import IMUOutput

class QuadState:
	
	def cam_cb(self, tag_pose):
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
		self.o_cam_in_tag = -rot_cam_in_tag.dot(o_tag_in_cam)
		self.q_cam_in_tag = Quaternion(matrix=rot_cam_in_tag)
		
		print self.o_cam_in_tag
		print self.q_cam_in_tag
	
	def imu_cb(self, imu_data):
		# Put ROS message in to numpy arrays
		self.accel = np.array([imu_data.accel_x, imu_data.accel_y,
							   imu_data.accel_z])
		self.gyro = np.array([imu_data.gyro_x, imu_data.gyro_y,
							  imu_data.gyro_z])
		print self.accel, self.gyro
		
	def __init__(self):
		self.quad_pose = Pose()
		self.send_pose = False
		
		# Subscribe to AprilTag publisher
		rospy.Subscriber("tag_detector/tag_pose", Pose, self.cam_cb)
		# Subscribe to IMU publisher
		rospy.Subscriber("imu_data", IMUOutput, self.imu_cb)
		# Create publisher for current pose estimate
		quad_pose_pub = rospy.Publisher("quad_pose", Pose, queue_size=10)
		
		while not rospy.is_shutdown():
			if self.send_pose:
				quad_pose_pub.publish(self.quad_pose)
				self.send_pose = False
	
if __name__ == '__main__':
	# Initialize node
	rospy.init_node('quad_state')

	try:
		quad_state = QuadState()
	except rospy.ROSInterruptException:
		pass

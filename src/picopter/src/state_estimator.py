#!/usr/bin/env python

import rospy
import time
import math
import scipy.linalg
import numpy as np
from picopter.msg import CamMeasurement

class StateEstimator:
	# Convert vectors from lab frame to body frame
	def lab_to_body(self, vec_lab, yaw_lab, pitch_lab, roll_lab):
		c1 = math.cos(yaw_lab)
		s1 = math.sin(yaw_lab)
		c2 = math.cos(pitch_lab)
		s2 = math.sin(pitch_lab)
		c3 = math.cos(roll_lab)
		s3 = math.sin(roll_lab)
		
		R_b_in_l =  np.array([[c1*c2, c1*s2*s3 - c3*s1, s1*s3 + c1*c3*s2],
							  [c2*s1, c1*c3 + s1*s2*s3, c3*s1*s2 - c1*s3],
							  [-s2, c2*s3, c2*c3]])
		vec_body = np.dot(R_b_in_l, vec_lab)
		
		return vec_body
		
	# Convert body rates to Euler rates
	def body_to_euler(self, imu_data):
		c2 = math.cos(imu_data[5])
		s2 = math.sin(imu_data[5])
		c3 = math.cos(imu_data[6])
		s3 = math.sin(imu_data[6])
		
		S = np.array([[0.0, s3, c3], 
					  [0.0, c2*c3, -c2*s3],
					  [c2, s2*s3, s2*c3]])
		S = (1/c2)*S
		
		theta_dots = np.dot(S, np.array([imu_data[9], 
										 imu_data[8], 
										 imu_data[7]]))
										 
		return theta_dots
		
	def velocity_est(self):
		if self.first_predict:
			self.last_x = self.cam_data[0]
			self.last_y = self.cam_data[1]
			self.last_z = self.cam_data[2]
			self.first_predict = False
			
			return 0., 0., 0.
		else:
			vel_x = (self.cam_data[0] - self.last_x)*self.dt
			vel_y = (self.cam_data[1] - self.last_y)*self.dt
			vel_z = (self.cam_data[2] - self.last_z)*self.dt
			self.last_x = self.cam_data[0]
			self.last_y = self.cam_data[1]
			self.last_z = self.cam_data[2]
			
			return vel_x, vel_y, vel_z
	
	def cam_cb(self, tag_pose):
		# Put ROS messages in to numpy arrays
		# z 6x1
		self.cam_data = np.array([tag_pose.x,
								  tag_pose.y,
								  tag_pose.z,
								  tag_pose.yaw,
								  tag_pose.pitch,
								  tag_pose.roll])
								  					  
		# print self.cam_data
		
		self.new_cam_data = True
		
	def get_state(self):
		imu_data = self.bno.get_imu_data()
		# Convert body rates to euler rates
		theta_dots = self.body_to_euler(imu_data)
		# Estimate positional velocities
		vel_x_l, vel_y_l, vel_z_l = self.velocity_est()
		# Convert state from lab frame to body frame
		#pos_b = self.lab_to_body(self.cam_data[0:3], self.cam_data[3], imu_data[5], imu_data[6])
		#vel_b = self.lab_to_body(np.array([vel_x_l, vel_y_l, vel_z_l]), self.cam_data[3], imu_data[5], imu_data[6])
		
		state = np.array([self.cam_data[0],
						  self.cam_data[1],
						  self.cam_data[2],
						  self.cam_data[3],
						  imu_data[5],
						  imu_data[6],
						  vel_x_l,
						  vel_y_l,
						  vel_z_l,
						  theta_dots[0],
						  theta_dots[1],
						  theta_dots[2]])
						  
		return state
	
	def __init__(self, quad, bno):
		self.bno = bno
		# Acceleration due to gravity in m/s^2
		self.g = 9.80665
		# Guess at tag_detector average report rate
		self.dt = 0.5
		
		self.first_predict = True
		self.new_cam_data = False
		
		
		

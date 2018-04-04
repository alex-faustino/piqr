#!/usr/bin/env python

import rospy
import time
import math
import scipy.linalg
import numpy as np
from picopter.msg import CamMeasurement

class StateEstimator:
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
		
		theta_dots = np.dot(S, np.array([[imu_data[9]], 
										 [imu_data[7]], 
										 [imu_data[8]]]))
										 
		return theta_dots
		
	def velocity_est(self):
		if self.first_predict:
			self.last_x = self.cam_data[0, 0]
			self.last_y = self.cam_data[1, 0]
			self.last_z = self.cam_data[2, 0]
			self.first_predict = False
			return 0., 0., 0.
		else:
			vel_x = (self.cam_data[0, 0] - self.last_x)*self.dt
			vel_y = (self.cam_data[1, 0] - self.last_y)*self.dt
			vel_z = (self.cam_data[2, 0] - self.last_z)*self.dt
			return vel_x, vel_y, vel_z
	
	def cam_cb(self, tag_pose):
		# Put ROS messages in to numpy arrays
		# z 6x1
		self.cam_data = np.array([[tag_pose.x],
								  [tag_pose.y],
								  [tag_pose.z],
								  [tag_pose.yaw],
								  [tag_pose.pitch],
								  [tag_pose.roll]])
								  					  
		# print self.cam_data
		
		self.new_cam_data = True
		
	def get_state(self):
		imu_data = self.bno.get_imu_data()
		# Convert body rates to euler rates
		theta_dots = self.body_to_euler(imu_data)
		vel_x, vel_y, vel_z = self.velocity_est()
		
		state = np.array([[self.cam_data[0, 0]],
						  [self.cam_data[1, 0]],
						  [self.cam_data[2, 0]],
						  [self.cam_data[3, 0]],
						  [imu_data[5]],
						  [imu_data[6]],
						  [vel_x],
						  [vel_y],
						  [vel_z],
						  [imu_data[9]],
						  [imu_data[7]],
						  [imu_data[8]]])
						  
		return state
	
	def predict(self, quad_state, imu_data):
		# Convert body rates to euler rates
		theta_dots = self.body_to_euler(imu_data)
		# Predict the next state
		# state_pred = np.dot(self.F, state) + np.dot(self.B, inputs)
		
		# Use trapezoidal integration on imu measurements to predict 
		# next state
		if self.first_predict:
			d_vel_x = np.trapz([0, imu_data[1]], dx=0.01)
			d_vel_y = np.trapz([0, imu_data[2]], dx=0.01)
			d_vel_z = np.trapz([0, imu_data[3]], dx=0.01)
			d_x = np.trapz([0, d_vel_x], dx=0.01)
			d_y = np.trapz([0, d_vel_y], dx=0.01)
			d_z = np.trapz([0, d_vel_z], dx=0.01)
		else:
			d_vel_x = np.trapz([self.acc_x_km1, imu_data[1]], dx=0.01)
			d_vel_y = np.trapz([self.acc_y_km1, imu_data[2]], dx=0.01)
			d_vel_z = np.trapz([self.acc_z_km1, imu_data[3]], dx=0.01)
			d_x = np.trapz([self.vel_x_km1, d_vel_x], dx=0.01)
			d_y = np.trapz([self.vel_y_km1, d_vel_y], dx=0.01)
			d_z = np.trapz([self.vel_z_km1, d_vel_z], dx=0.01)
		
		d_quad_state = np.array([[d_x],
								 [d_y],
								 [d_z],
								 [0], [0], [0],
								 [d_vel_x],
								 [d_vel_y],
								 [d_vel_z],
								 [0], [0], [0]])
								 
		state_pred = quad_state + d_quad_state
		
		# Cycle imu values
		self.acc_x_km1 = imu_data[1]
		self.acc_y_km1 = imu_data[2]
		self.acc_z_km1 = imu_data[3]
		self.vel_x_km1 = d_vel_x
		self.vel_y_km1 = d_vel_y
		self.vel_z_km1 = d_vel_z
		
		# Propogate state covariance
		self.P = np.dot(np.dot(self.F, self.P), self.F.T) + self.Q
		
		return state_pred
		
	def update(self, quad_state):
		# Localize matricies for readability and speed boost
		z = self.cam_data
		R = self.R
		H = self.H
		P = self.P
		x = quad_state
		# Identity matrix
		I = np.eye(12)
		
		# Compute residual
		self.y = z - np.dot(H, x)
		
		# PH'
		PHT = np.dot(P, H.T)
		
		# S = HPH' + R
		self.S = np.dot(H, PHT) + R
		
		# K = PH'S^-1
		self.K = np.dot(PHT, scipy.linalg.inv(self.S))
		
		# x = x + Ky
		state_pred = x + np.dot(self.K, self.y)
		
		# P = (I - KH)P(I - KH)' + KRK'
		IKH = I - np.dot(self.K, H)
		self.P = np.dot(np.dot(IKH, P), IKH.T) + np.dot(np.dot(self.K, R), self.K.T)
		
		return state_pred
		
	def __init__(self, quad, bno):
		self.bno = bno
		# Acceleration due to gravity in m/s^2
		self.g = 9.80665
		# Guess at tag_detector average report rate
		self.dt = 0.5
		# State covariance matrix 12x12
		self.P = np.diag([1., 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1]) 
		# State transfer function matrix 12x12
		self.F = np.array([[1., 0, 0, 0, -self.g*self.dt, 0, self.dt, 0, 0, 0, 0, 0], 
						   [0, 1, 0, 0, 0, self.g*self.dt, 0, self.dt, 0, 0, 0, 0],
						   [0, 0, 1, 0, 0, 0, 0, 0, self.dt, 0, 0, 0],
						   [0, 0, 0, 1, 0, 0, 0, 0, 0, self.dt, 0, 0],
						   [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, self.dt, 0],
						   [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, self.dt],
						   [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
						   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
						   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
						   [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
						   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
						   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])
		# Process covariance 12x12
		self.Q = np.diag([0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01])
		# Control function 12x4
		self.B = np.array([[0., 0, 0, 0],
						   [0, 0, 0, 0],
						   [0, 0, 0, 0],
						   [0, 0, 0, 0],
						   [0, 0, 0, 0],
						   [0, 0, 0, 0],
						   [0, 0, 0, 0],
						   [0, 0, 0, 0],
						   [0, 0, 0, -self.dt/quad.m],
						   [0, 0, self.dt/quad.j_yaw, 0],
						   [0, self.dt/quad.j_pitch, 0, 0],
						   [self.dt/quad.j_roll, 0, 0, 0]])
		# Measurement function 6x12
		self.H = np.array([[1., 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
						   [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
						   [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
						   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
						   [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
						   [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]])
		# Measurement noise covariance 6x6
		self.R = np.diag([0.1, 0.1, 0.1, 0.01, 0.01, 0.01])
		# Kalman gain 12x6
		self.K = np.zeros((12, 6))
		# Residual 6x1
		self.y = np.zeros((6, 1))
		# System uncertainty 6x6
		self.S = np.zeros((6, 6))
		
		self.first_predict = True
		self.new_cam_data = False
		
		
		

import time
import math
import scipy.linalg

import numpy as np

class QuadController:
	# Observe position error and compute desired roll, pitch, yaw, and
	# thrust
	def postion_control(self, inputs_nominal, quad_state):
		roll_desired = np.dot(-self.K_y, np.array([quad_state[1], 
												   quad_state[7]]))
		pitch_desired = np.dot(-self.K_x, np.array([quad_state[0], 
												   quad_state[6]]))
		yaw_desired = 0.0
		thrust_delta = np.dot(-self.K_z, np.array([quad_state[2], 
												   quad_state[8]]))
		inputs_delta = np.vstack((roll_desired, pitch_desired, yaw_desired, thrust_delta))
								 
		inputs = inputs_nominal + inputs_delta
		
		return inputs
	
	# Regulate attitude
	def attitude_control(self, position_inputs, quad_state):
		roll_torque = np.dot(-self.K_roll, np.array([quad_state[5] - position_inputs[0], 
												     quad_state[11]]))
		pitch_torque = np.dot(-self.K_pitch, np.array([quad_state[4] + position_inputs[1], 
												       quad_state[10]]))
		yaw_torque = np.dot(-self.K_yaw, np.array([quad_state[3] - position_inputs[2], 
												   quad_state[9]]))
		inputs = np.vstack((roll_torque, pitch_torque, yaw_torque, position_inputs[3]))
		
		return inputs
		
	# Convert from thrusts and torques to spin rates
	def input_to_spin(self, inputs, quad):
		k_M = quad.k_M
		k_F = quad.k_F
		lx = quad.lx
		ly = quad.ly
		
		W = np.array([[k_F*ly,-k_F*ly,k_F*ly,-k_F*ly],
					  [k_F*lx,k_F*lx,-k_F*lx,-k_F*lx],
					  [k_M, -k_M, -k_M, k_M],
					  [-k_F, -k_F, -k_F, -k_F]])

		spin_rates = scipy.linalg.solve(W, inputs)
		
		return spin_rates
		 
	# Solve discrete time LQR controller
	def dlqr(self, A, B, Q, R):
		# Reference Bertsekas, p.151
		# Code reference kostasalexis.com/lqr-control.html
		
		# Try to solve the ricatti equation
		X = np.matrix(scipy.linalg.solve_discrete_are(A, B, Q, R))
		
		# Compute the LQR gain
		K = np.array(scipy.linalg.inv(B.T*X*B + R)*(B.T*X*A))
		
		return K
		
	# Set up all necessary controller gains
	def compute_gains(self, quad):
		# Position
		# x
		A_x = np.array([[1, self.dt], [0, 1]])
		B_x = np.array([[0], [-self.g*self.dt]])
		Q_x = np.array([[1.6, 0], [0, 0.5]])
		R_x = np.array([30.0])
		self.K_x = self.dlqr(A_x, B_x, Q_x, R_x)
		
		# y
		A_y = np.array([[1, self.dt], [0, 1]])
		B_y = np.array([[0], [self.g*self.dt]])
		Q_y = np.array([[1.6, 0], [0, 0.5]])
		R_y = np.array([30.0])
		self.K_y = self.dlqr(A_y, B_y, Q_y, R_y)
		
		# z
		A_z = np.array([[1, self.dt], [0, 1]])
		B_z = np.array([[0], [-self.dt/quad.m]])
		Q_z = np.array([[35.0, 0], [0, 4.0]])
		R_z = np.array([0.3])
		self.K_z = self.dlqr(A_z, B_z, Q_z, R_z)
		
		# Attitude
		# roll
		A_roll = np.array([[1, self.dt], [0, 1]])
		B_roll = np.array([[0], [self.dt/quad.j_roll]])
		Q_roll = np.array([[20.0, 0], [0, 0.8]])
		R_roll = np.array([0.7])
		self.K_roll = self.dlqr(A_roll, B_roll, Q_roll, R_roll)
		
		# pitch
		A_pitch = np.array([[1, self.dt], [0, 1]])
		B_pitch = np.array([[0], [self.dt/quad.j_pitch]])
		Q_pitch = np.array([[30.0, 0], [0, 0.6]])
		R_pitch = np.array([0.7])
		self.K_pitch = self.dlqr(A_pitch, B_pitch, Q_pitch, R_pitch)
		
		# yaw
		A_yaw = np.array([[1, self.dt], [0, 1]])
		B_yaw = np.array([[0], [self.dt/quad.j_yaw]])
		Q_yaw = np.array([[5.0, 0], [0, 0.6]])
		R_yaw = np.array([1.8])
		self.K_yaw = self.dlqr(A_yaw, B_yaw, Q_yaw, R_yaw)
		
	def __init__(self, quad):
		# Acceleration due to gravity in m/s^2
		self.g = 9.8066
		# Average dt estimate
		self.dt = 0.005
		
		self.compute_gains(quad)
		
		

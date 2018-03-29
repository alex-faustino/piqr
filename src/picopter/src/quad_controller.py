import time
import scipy.linalg

import numpy as np

from pid import PID

class QuadController:
	# Observe position error and compute desired roll, pitch, yaw, and
	# thrust
	def outer_loop(self, inputs_nominal, quad_state):
		self.roll_desired = np.dot(-self.K_roll, np.array([[quad_state.y], [quad_state.y_dot]]))
		
		
	# Convert from thrusts and torques to spin rates
	def input_to_spin(self, inputs):
		# Proportionality constants between spin rate and pwm
		# Determined in Lab
		# TODO: Replace placeholder k_M and k_F
		k_M = 1.13e-7 
		k_F = 5.46e-5
		
		W = np.array([[k_F*self.ly,-k_F*self.ly,k_F*self.ly,-k_F*self.ly],
					  [k_F*self.lx,k_F*self.lx,-k_F*self.lx,-k_F*self.lx],
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
	def compute_gains(self):
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
		B_z = np.array([[0], [-1/self.m*self.dt]])
		Q_z = np.array([[35.0, 0], [0, 4.0]])
		R_z = np.array([0.3])
		self.K_z = self.dlqr(A_z, B_z, Q_z, R_z)
		
		# Attitude
		# roll
		A_roll = np.array([[1, self.dt], [0, 1]])
		B_roll = np.array([[0], [self.dt/self.j_roll]])
		Q_roll = np.array([[20.0, 0], [0, 0.8]])
		R_roll = np.array([0.7])
		self.K_roll = self.dlqr(A_roll, B_roll, Q_roll, R_roll)
		print self.K_roll
		
		# pitch
		A_pitch = np.array([[1, self.dt], [0, 1]])
		B_pitch = np.array([[0], [self.dt/self.j_pitch]])
		Q_pitch = np.array([[30.0, 0], [0, 0.6]])
		R_pitch = np.array([0.7])
		self.K_pitch = self.dlqr(A_pitch, B_pitch, Q_pitch, R_pitch)
		
		# yaw
		A_yaw = np.array([[1, self.dt], [0, 1]])
		B_yaw = np.array([[0], [self.dt/self.j_yaw]])
		Q_yaw = np.array([[5.0, 0], [0, 0.6]])
		R_yaw = np.array([1.8])
		self.K_yaw = self.dlqr(A_yaw, B_yaw, Q_yaw, R_yaw)
		
	def __init__(self):
		# Quad mass in kg
		self.m = 1.0 # temp
		# Acceleration due to gravity in m/s^2
		self.g = 9.80665
		# Spar lengths in m
		self.lx = 0.28575/2
		self.ly = 0.3556/2
		# Average dt estimate
		self.dt = 0.005
		# Moments of Inertia
		# TODO: Update to correct values
		self.j_roll = 0.004093
		self.j_pitch = 0.003944
		self.j_yaw = 0.007593
		
		self.compute_gains()
		
		

import numpy as np

class QuadState:

	def __init__(self):
		self.x = 0.0
		self.y = 0.0
		self.z = 0.0
		self.yaw = 0.0
		self.pitch = 0.0
		self.roll = 0.0
		self.x_dot = 0.0
		self.y_dot = 0.0
		self.z_dot = 0.0
		self.yaw_rate = 0.0
		self.pitch_rate = 0.0
		self.roll_rate = 0.0
		
		self.state = np.array([[self.x], 
							   [self.y],
							   [self.z],
							   [self.yaw],
							   [self.pitch],
							   [self.roll],
							   [self.x_dot],
							   [self.y_dot],
							   [self.z_dot],
							   [self.yaw_rate],
							   [self.pitch_rate],
							   [self.roll_rate]])

class Quadcopter:
	
	def __init__(self, m, lx, ly, j_roll, j_pitch, j_yaw, k_M, k_F):
		# Quad mass in kg
		self.m = m # temp
		
		# Spar lengths in m
		self.lx = lx
		self.ly = ly
		
		# Moments of Inertia
		# TODO: Update to correct values
		self.j_roll = j_roll
		self.j_pitch = j_pitch
		self.j_yaw = j_yaw
		
		# Proportionality constants between spin rate and pwm
		# Determined in Lab
		# TODO: Replace placeholder k_M and k_F
		self.k_M = k_M 
		self.k_F = k_F
		

class PID:
	def compute(self, input, target, dt):
		error = target - input
		
		err_p = error
		
		self.err_i += (error + self.prev_error)*dt
		err_i = self.err_i
		
		err_d = (error - self.prev_error)/dt
		
		output_p = self.k_p*err_p
		output_i = self.k_i*err_i
		output_d = self.k_d*err_d
		
		self.prev_error = error
		
		return output_p, output_i, output_d
		
	def __init__(self, k_p, k_i, k_d):
		self.k_p = k_p
		self.k_i = k_i
		self.k_d = k_d
		
		self.prev_error = 0.0
		self.err_i = 0.0

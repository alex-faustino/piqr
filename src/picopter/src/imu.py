import time
import math
import numpy as np

from Adafruit_BNO055 import BNO055

class Imu:
	def get_imu_data(self):
		t = time.time()
		accel_x, accel_y, accel_z = self.bno.read_linear_acceleration()
		yaw, roll, pitch = self.bno.read_euler()
		# fix pitch mod
		if pitch < 0:
			pitch += 180
		else:
			pitch -= 180
		yaw = math.radians(yaw)
		pitch = math.radians(pitch)
		roll = math.radians(roll)
		gyro_x, gyro_y, gyro_z = self.bno.read_gyroscope()
		gyro_x = math.radians(gyro_x)
		gyro_y = math.radians(gyro_y)
		gyro_z = math.radians(gyro_z)
		
		imu_data = np.array([t, accel_x, accel_y, accel_z, yaw, pitch, roll, gyro_x, gyro_y, gyro_z])
		
		return imu_data
		
	def __init__(self):
		# Raspberry Pi configuration with serial UART and RST connected to GPIO 18:
		self.bno = BNO055.BNO055(serial_port='/dev/ttyAMA0', rst=18)

		if not self.bno.begin():
			raise RuntimeError('Failed to initialize BNO055')
		
		# Adjust IMU frame since it is mounted 90 degrees to what is expected
		self.bno.set_axis_remap(0, 1, 2, 1, 0, 1)
		
			

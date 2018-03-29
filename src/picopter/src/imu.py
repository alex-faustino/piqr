import time

from Adafruit_BNO055 import BNO055

class Imu:
	def get_imu_data(self):
		t = time.time()
		accel_x, accel_y, accel_z = self.bno.read_accelerometer()
		gyro_x, gyro_y, gyro_z = self.bno.read_gyroscope()
		
		return t, accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z
		
	def __init__(self):
		# Raspberry Pi configuration with serial UART and RST connected to GPIO 18:
		self.bno = BNO055.BNO055(serial_port='/dev/ttyAMA0', rst=18)

		if not self.bno.begin():
			raise RuntimeError('Failed to initialize BNO055')
		
		# Adjust IMU frame since it is mounted 90 degrees to what is expected
		self.bno.set_axis_remap(0, 1, 2, 0, 1, 1)
		
			

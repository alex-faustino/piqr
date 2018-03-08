#!/usr/bin/env python

import rospy
import time

from Adafruit_BNO055 import BNO055
from picopter.msg import IMUOutput

# Raspberry Pi configuration with serial UART and RST connected to GPIO 18:
bno = BNO055.BNO055(serial_port='/dev/ttyAMA0', rst=18)

if not bno.begin():
	raise RuntimeError('Failed to initialize BNO055')
# Adjust IMU frame since it is mounted 90 degrees to what is expected
# BNO055.BNO055.set_axis_remap(bno, 1, 0, 2, x_sign=0, y_sign=1, z_sign=0)

def publish_data():
	data_pub = rospy.Publisher('imu_data', IMUOutput, queue_size=10)
	rospy.init_node('imu_data')
	rate = rospy.Rate(90)
	while not rospy.is_shutdown():
		imu_msg = IMUOutput()
		imu_msg.time = time.time()
		imu_msg.accel_x,imu_msg.accel_y,imu_msg.accel_z = bno.read_accelerometer()
		imu_msg.gyro_x,imu_msg.gyro_y,imu_msg.gyro_z = bno.read_gyroscope()
		data_pub.publish(imu_msg)
		print(imu_msg)
		rate.sleep()
		
if __name__ == "__main__":
	try:
		publish_data()
	except rospy.ROSInterruptException:
		pass

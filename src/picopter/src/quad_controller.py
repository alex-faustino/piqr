#!/usr/bin/env python

import rospy
from picopter.msg import SpinRates
from picopter.msg import Interface
from geometry_msgs.msg import Point

class QuadController:
	
	# Switch to flight mode
	def interface_cb(self, flags):
		if flags.flight_mode and flags.is_calibrated:
			self.flight_mode = True
			
	# Track path from flight planner
	def path_cb(self, loc_desired):
		self.send_rates = True
		
	def __init__(self):
		self.flight_mode = False
		self.spin_rates = SpinRates()
		self.send_rates = True
		
		# Test values
		self.spin_rates.motor_one = 1100
		self.spin_rates.motor_two = 1100
		self.spin_rates.motor_three = 1100
		self.spin_rates.motor_four = 1100
		
		# Subscribe to interface topic
		rospy.Subscriber("interface_flags", Interface, self.interface_cb)
		# Subscribe to planner publisher
		rospy.Subscriber("cmd_path", Point, self.path_cb)
		# Create publisher for spin rate cmd
		spin_rates_pub = rospy.Publisher("cmd_spin", SpinRates, queue_size=10)
		
		while not rospy.is_shutdown():
			if self.flight_mode:
				if self.send_rates:
					spin_rates_pub.publish(self.spin_rates)
					self.send_rates = False

if __name__ == '__main__':
	# Initialize node
	rospy.init_node('quad_controller')

	try:
		quad_controller = QuadController()
	except rospy.ROSInterruptException:
		pass

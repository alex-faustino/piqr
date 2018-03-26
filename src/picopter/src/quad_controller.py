#!/usr/bin/env python

import rospy
from picopter.msg import SpinRates
from geometry_msgs.msg import Point

class QuadController:
			
	# Track path from flight planner
	def path_cb(self, loc_desired):
		self.send_rates = True
		
	def __init__(self):
		self.rate = rospy.Rate(50)
		self.spin_rates = SpinRates()
		self.send_rates = True
		
		# Test values
		self.spin_rates.motor_one = 700
		self.spin_rates.motor_two = 700
		self.spin_rates.motor_three = 700
		self.spin_rates.motor_four = 700
		
		# Subscribe to planner publisher
		rospy.Subscriber("cmd_path", Point, self.path_cb)
		# Create publisher for spin rate cmd
		spin_rates_pub = rospy.Publisher("cmd_spin", SpinRates, queue_size=10)
		
		while not rospy.is_shutdown():
			if self.send_rates:
				spin_rates_pub.publish(self.spin_rates)
				self.send_rates = False
			self.rate.sleep()
				

if __name__ == '__main__':
	# Initialize node
	rospy.init_node('quad_controller')

	try:
		quad_controller = QuadController()
	except rospy.ROSInterruptException:
		pass

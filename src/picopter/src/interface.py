#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Point
from picopter.msg import Interface

class PicopterInterface:
	
	def __init__(self):
		self.rate = rospy.Rate(0.05) # 20 seconds
		self.flags = Interface()
		self.goal = Point()
		
		# Create publisher for user interface flags and goal location
		flags_pub = rospy.Publisher("interface_flags", Interface, queue_size=10)
		goal_pub = rospy.Publisher("goal_loc", Point, queue_size=10)
		
		while True:
			print('Need to calibrate the ESC? Y or N')
			inp = raw_input()
			if inp == 'Y' or inp == 'y':
				self.flags.is_calibrated = False
				self.flags.flight_mode = False
				break
			elif inp == 'N' or inp == 'n':
				self.flags.is_calibrated = True
				self.flags.flight_mode = True
				break
			else:
				print "Invalid input."
				
		while not rospy.is_shutdown():
			if not self.flags.is_calibrated:
				flags_pub.publish(self.flags)
				self.flags.is_calibrated = True
				self.flags.flight_mode = True
			else:
				flags_pub.publish(self.flags)
				
			self.rate.sleep()

if __name__ == '__main__':
	# Initialize node
	rospy.init_node('interface')

	try:
		interface = PicopterInterface()
	except rospy.ROSInterruptException:
		pass

#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Point

class FlightPlanner:
			
	def __init__(self):
		self.flight_mode = False
		self.loc_desired = Point()
		self.send_loc = True
		
		# Test values
		self.loc_desired.x = 0
		self.loc_desired.y = 0
		self.loc_desired.z = 0
		
		# Subscribe to planner publisher
		# rospy.Subscriber("goal_loc", Point, self.goal_cb)
		# Create publisher for spin rate cmd
		loc_desired_pub = rospy.Publisher("cmd_path", Point, queue_size=10)
		
		while not rospy.is_shutdown():
			if self.send_loc:
				loc_desired_pub.publish(self.loc_desired)
				self.send_loc = False

if __name__ == '__main__':
	# Initialize node
	rospy.init_node('flight_planner')

	try:
		flight_planner = FlightPlanner()
	except rospy.ROSInterruptException:
		pass

#!/usr/bin/env python

import rospy
import time
from geometry_msgs.msg import Point
from picopter.msg import Interface

class PicopterInterface:
	
	def __init__(self):
		self.rate = rospy.Rate(0.05) # 20 seconds
		
		# Initialize all flags to false
		self.flags = Interface()
		self.flags.is_calibrated = False
		self.flags.arm_esc = False
		self.flags.flight_mode = False
		self.flags.stop_motors = False
		self.flags.shutdown = False
		
		# Initialize hover location in world frame
		self.goal = Point()
		
		# Create publisher for user interface flags and goal location
		flags_pub = rospy.Publisher("interface_flags", Interface, queue_size=10)
		goal_pub = rospy.Publisher("goal_loc", Point, queue_size=10)
		
		print "Command options:"
		print "1. Calibrate"
		print "2. Arm"
		print "3. Fly"
		print "4. Stop"
		print "5. Shutdown"
		
		#while True:
			#print('Need to calibrate the ESC? Y or N')
			#inp = raw_input()
			#if inp == 'Y' or inp == 'y':
				#self.flags.is_calibrated = False
				#self.flags.flight_mode = False
				#break
			#elif inp == 'N' or inp == 'n':
				#self.flags.is_calibrated = True
				#self.flags.flight_mode = True
				#break
			#else:
				#print "Invalid input."
				
		#~ while not rospy.is_shutdown():
			#~ if not self.flags.is_calibrated:
				#~ flags_pub.publish(self.flags)
				#~ self.flags.is_calibrated = True
				#~ self.flags.flight_mode = True
			#~ else:
				#~ flags_pub.publish(self.flags)
				
			#~ self.rate.sleep()
		
		while not rospy.is_shutdown():
			print "Command: "
			inp = raw_input()
			if any ( [inp == '1', inp == 'calibrate', inp == 'Calibrate']): 
				self.flags.is_calibrated = False
				self.flags.arm_esc = False
				self.flags.flight_mode = False
				self.flags.stop_motors = False
				self.flags.shutdown = False
				wait_time = 25
			if any ( [inp == '2', inp == 'arm', inp == 'Arm']): 
				self.flags.is_calibrated = True
				self.flags.arm_esc = True
				self.flags.flight_mode = False
				self.flags.stop_motors = False
				self.flags.shutdown = False
				wait_time = 5
			if any ( [inp == '3', inp == 'fly', inp == 'Fly']): 
				self.flags.is_calibrated = True
				self.flags.arm_esc = False
				self.flags.flight_mode = True
				self.flags.stop_motors = False
				self.flags.shutdown = False
			if any ( [inp == '4', inp == 'stop', inp == 'Stop']): 
				self.flags.is_calibrated = True
				self.flags.arm_esc = False
				self.flags.flight_mode = False
				self.flags.stop_motors = True
				self.flags.shutdown = False
			if any ( [inp == '5', inp == 'shutdown', inp == 'Shutdown']): 
				self.flags.is_calibrated = True
				self.flags.arm_esc = False
				self.flags.flight_mode = False
				self.flags.stop_motors = True
				self.flags.shutdown = True
			flags_pub.publish(self.flags)
			time.sleep(wait_time)
			
if __name__ == '__main__':
	# Initialize node
	rospy.init_node('interface')

	try:
		interface = PicopterInterface()
	except rospy.ROSInterruptException:
		pass

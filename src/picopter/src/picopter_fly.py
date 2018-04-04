#!/usr/bin/env python

import rospy
import os
import sys
import time

import numpy as np

from quadcopter import Quadcopter
from imu import Imu
from motor_controller import MotorController
from quad_controller import QuadController
from flight_planner import FlightPlanner
from state_estimator import StateEstimator
from quad_state import QuadState
from picopter.msg import CamMeasurement

# Launch GPIO library
os.system ("sudo pigpiod")
time.sleep(1.5)
		
class PicopterFly:
	
	def __init__(self, bno, mc, qc, fp, se):
		self.bno = bno
		self.mc = mc
		self.qc = qc
		self.fp = fp
		self.se = se
		self.quad_state = QuadState()
		
		self.mc.motors_start()
		self.mc.motors_arm()
		
		# Subscribe to AprilTag publisher
		rospy.Subscriber("tag_detector/tag_pose", CamMeasurement, se.cam_cb)
		
		while not rospy.is_shutdown():
			if self.se.new_cam_data:
				self.quad_state.state = self.se.update(self.quad_state.state)
				# print self.quad_state.state
			else:
				self.quad_state.state = self.se.predict(self.quad_state.state, self.bno.get_imu_data())
		
		self.mc.motors_stop()
		

if __name__ == '__main__':
	# Initialize node
	rospy.init_node('picopter')
	
	try:
		picopter = Quadcopter(1, 0.28575/2, 0.3556/2, 0.004093, 0.003944, 0.007593, 1.13e-7, 5.46e-5)
		bno = Imu()
		mc = MotorController()
		qc = QuadController(picopter)
		fp = FlightPlanner()
		se = StateEstimator(picopter)
		picopter_fly = PicopterFly(bno, mc, qc, fp, se)
	except rospy.ROSInterruptException:
		pass

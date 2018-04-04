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
from picopter.msg import CamMeasurement

# Launch GPIO library
os.system ("sudo pigpiod")
time.sleep(1.5)
		
class PicopterFly:
	
	def __init__(self, bno, mc, qc, fp, se, quad):
		self.bno = bno
		self.mc = mc
		self.qc = qc
		self.fp = fp
		self.se = se
		self.quad = quad
		
		# Acceleration due to gravity in m/s^2
		self.g = 9.8066
		
		self.mc.motors_start()
		self.mc.motors_arm()
		
		# Subscribe to AprilTag publisher
		rospy.Subscriber("tag_detector/tag_pose", CamMeasurement, se.cam_cb)
		
		# Hover test nominal input
		inputs_nominal = np.array([[0], [0], [0], [-self.quad.m*self.g]])
		
		while not self.se.new_cam_data:
			print "Waiting for first tag detection..."
			
		while not rospy.is_shutdown():
			if self.se.new_cam_data:
				self.quad_state = self.se.get_state()
				position_control_inputs = self.qc.postion_control(inputs_nominal, self.quad_state)
				self.se.new_cam_data = False
			else:
				self.quad_state = self.se.get_state()
				attitude_control_inputs = self.qc.attitude_control(position_control_inputs, self.quad_state)
				# print attitude_control_inputs
				spin_rates = self.qc.input_to_spin(attitude_control_inputs, self.quad)
				# print spin_rates
				mc.set_pwm(mc.esc_one, spin_rates[0])
				mc.set_pwm(mc.esc_two, spin_rates[1])
				mc.set_pwm(mc.esc_three, spin_rates[2])
				mc.set_pwm(mc.esc_four, spin_rates[3])
				
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
		se = StateEstimator(picopter, bno)
		picopter_fly = PicopterFly(bno, mc, qc, fp, se, picopter)
	except rospy.ROSInterruptException:
		pass

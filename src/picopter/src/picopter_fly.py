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
		inputs_nominal = np.array([0., 0, 0, -self.quad.m*self.g])
		
		while not self.se.new_cam_data:
			print "Waiting for first tag detection..."
			
		test_pwm = 1200
		# hover_pwm = 1560
		keep_testing = True
		while keep_testing:
			
			# Control test block
			if self.se.new_cam_data:
				self.quad_state = self.se.get_state()
				# print self.quad_state
				position_control_inputs = self.qc.postion_control(inputs_nominal, self.quad_state)
				self.se.new_cam_data = False
			else:
				self.quad_state = self.se.get_state()
				attitude_control_inputs = self.qc.attitude_control(position_control_inputs, self.quad_state)
				#print attitude_control_inputs
				spin_rates = self.qc.input_to_spin(attitude_control_inputs, self.quad)
				#print spin_rates
				mc.set_pwm(mc.esc_one, spin_rates[0])
				mc.set_pwm(mc.esc_two, spin_rates[1])
				mc.set_pwm(mc.esc_three, spin_rates[2])
				mc.set_pwm(mc.esc_four, spin_rates[3])
			"""
			# PWM hover test block
			# mc.set_pwm(mc.esc_one, test_pwm)
			# mc.set_pwm(mc.esc_two, test_pwm)
			# mc.set_pwm(mc.esc_three, test_pwm)
			mc.set_pwm(mc.esc_four, test_pwm)
			inp = raw_input()
			if inp == 'stop':
				keep_testing = False
			elif inp == 'd':
				test_pwm -= 50
			elif inp == 'u':
				test_pwm += 50
			else:
				pass
			"""
		self.mc.motors_stop()
		

if __name__ == '__main__':
	# Initialize node
	rospy.init_node('picopter')
	
	try:
		picopter = Quadcopter(1.1, 0.3556/2, 0.28575/2, 0.008465, 0.0154223, 0.023367, 1.13e-8, 8.300e-8)
		bno = Imu()
		mc = MotorController()
		qc = QuadController(picopter)
		fp = FlightPlanner()
		se = StateEstimator(picopter, bno)
		picopter_fly = PicopterFly(bno, mc, qc, fp, se, picopter)
	except rospy.ROSInterruptException:
		pass

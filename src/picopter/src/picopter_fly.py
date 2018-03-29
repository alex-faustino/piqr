#!/usr/bin/env python

import rospy
import os
import sys
import time

import numpy as np

from imu import Imu
from motor_controller import MotorController
from quad_controller import QuadController
from flight_planner import FlightPlanner

# Launch GPIO library
os.system ("sudo pigpiod")
time.sleep(1.5)
		
class Picopter:
	
	def __init__(self, bno, mc, qc, fp):
		self.bno = bno
		self.mc = mc
		self.qc = qc
		self.fp = fp
		
		self.mc.motors_start()
		self.mc.motors_arm()
		
		while not rospy.is_shutdown():
			for esc in self.mc.esc_list:
				print self.bno.get_imu_data()
				self.mc.set_pwm(esc, 1100)
			time.sleep(5)
			
			for esc in self.mc.esc_list:
				print self.bno.get_imu_data()
				self.mc.set_pwm(esc, 1500)
			time.sleep(5)
			
			for esc in self.mc.esc_list:
				print self.bno.get_imu_data()
				self.mc.set_pwm(esc, 1300)
			time.sleep(5)
			
			for esc in self.mc.esc_list:
				print self.bno.get_imu_data()
				self.mc.set_pwm(esc, 1700)
			time.sleep(5)
			
			for esc in self.mc.esc_list:
				print self.bno.get_imu_data()
				self.mc.set_pwm(esc, 1400)
			time.sleep(5)
		
		self.mc.motors_stop()
		

if __name__ == '__main__':
	# Initialize node
	rospy.init_node('picopter')
	
	try:
		bno = Imu()
		mc = MotorController()
		qc = QuadController()
		fp = FlightPlanner()
		picopter = Picopter(bno, mc, qc, fp)
	except rospy.ROSInterruptException:
		pass

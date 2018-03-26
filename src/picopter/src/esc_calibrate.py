#!/usr/bin/env python

import rospy
import os
import pigpio
import time

# launch GPIO
os.system ("sudo pigpiod")
time.sleep(1.5)

class ESCCalibrate:
	# Initialize motors
	def motors_start(self):
		self.pi.set_servo_pulsewidth(self.motor_one, 0)
		self.pi.set_servo_pulsewidth(self.motor_two, 0)
		self.pi.set_servo_pulsewidth(self.motor_three, 0)
		self.pi.set_servo_pulsewidth(self.motor_four, 0)
		
	# Set all motors to min_val
	def motors_min(self):
		self.pi.set_servo_pulsewidth(self.motor_one, self.min_val)
		self.pi.set_servo_pulsewidth(self.motor_two, self.min_val)
		self.pi.set_servo_pulsewidth(self.motor_three, self.min_val)
		self.pi.set_servo_pulsewidth(self.motor_four, self.min_val)
		
	# Set all motors to max_val
	def motors_max(self):
		self.pi.set_servo_pulsewidth(self.motor_one, self.max_val)
		self.pi.set_servo_pulsewidth(self.motor_two, self.max_val)
		self.pi.set_servo_pulsewidth(self.motor_three, self.max_val)
		self.pi.set_servo_pulsewidth(self.motor_four, self.max_val)
	
	# Stop all motors
	def motors_stop(self): 
		self.pi.set_servo_pulsewidth(self.motor_one, 0)
		self.pi.set_servo_pulsewidth(self.motor_two, 0)
		self.pi.set_servo_pulsewidth(self.motor_three, 0)
		self.pi.set_servo_pulsewidth(self.motor_four, 0)
		self.pi.stop()
		os.system ("sudo killall pigpiod")
		
	#This is the auto calibration procedure of a normal ESC
	def motors_calibrate(self):
		
		self.motors_start()
		print "Make sure the battery switch is OFF then press Enter"
		inp = raw_input()
		if inp == '':
			self.motors_max()
			print "Switch the battery ON."
			print "Wait for the beeping to stop then press Enter"
			inp = raw_input()
		if inp == '':
			self.motors_min()
			print "More beeping"
			time.sleep(7)
			print "Wait for it ...."
			time.sleep (5)
			print "Im working on it, ....."
			self.motors_start()
			time.sleep(2)
			print "Arming ESC now..."
			self.motors_min()
			time.sleep(1)
			print "Calibration Complete."
			self.motors_stop()
			time.sleep(1)
	
	def __init__(self):
		# GPIO pin number and wire color
		self.motor_one = 6 # yellow wire
		self.motor_two = 13 # orange
		self.motor_three = 19 # white
		self.motor_four = 26 # blue
		self.max_val = 2000 #max PWM
		self.min_val = 700  #min PWM
		self.pi = pigpio.pi()
		
		self.motors_calibrate()

if __name__ == '__main__':
	# Initialize node
	rospy.init_node('esc_calibrate')

	try:
		esc_calibrate = ESCCalibrate()
	except rospy.ROSInterruptException:
		pass

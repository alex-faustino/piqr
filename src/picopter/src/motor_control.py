#!/usr/bin/env python

import rospy
import os
import pigpio
import time
from picopter.msg import SpinRates
from picopter.msg import Interface

# launch GPIO
os.system ("sudo pigpiod")
time.sleep(1.5)

class MotorControl:
    
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
		
	# Arming procedure of an ESC
	def motors_arm(self): 
		print('Arming Motors - Should hear two beeps')
		self.motors_max()
		time.sleep(1.5)
		self.motors_min()
		time.sleep(1)
		print('Motors Armed')
		
	# Switch the motor contoller between modes
	def interface_cb(self, flags):
		if not flags.is_calibrated:
			self.motors_calibrate()
		if flags.arm_esc and flags.is_calibrated:
			self.motors_start()
			self.motors_arm()
		if flags.flight_mode and flags.is_calibrated:
			self.flight_mode = True
		if flags.shutdown:
			self.motors_stop()
			
	# Update the PWM of the motors
	def control_cb(self, spin_rates): 
		max_cur = 1500
		min_cur = 1100
		speed_one = spin_rates.motor_one
		speed_two = spin_rates.motor_two
		speed_three = spin_rates.motor_three
		speed_four = spin_rates.motor_four
		
		if self.flight_mode:
			if speed_one > max_cur:
				speed_one = max_cur
			if speed_one < min_cur:
				speed_one = min_cur
			if speed_two > max_cur:
				speed_two = max_cur
			if speed_two < min_cur:
				speed_two = min_cur
			if speed_three > max_cur:
				speed_three = max_cur
			if speed_three < min_cur:
				speed_three = min_cur
			if speed_four > max_cur:
				speed_four = max_cur
			if speed_four < min_cur:
				speed_four = min_cur
			  
			self.pi.set_servo_pulsewidth(self.motor_one, speed_one)
			self.pi.set_servo_pulsewidth(self.motor_two, speed_two)
			self.pi.set_servo_pulsewidth(self.motor_three, speed_three)
			self.pi.set_servo_pulsewidth(self.motor_four, speed_four)
    
    # Stop all motors
	def motors_stop(self): 
		self.pi.set_servo_pulsewidth(self.motor_one, 0)
		self.pi.set_servo_pulsewidth(self.motor_two, 0)
		self.pi.set_servo_pulsewidth(self.motor_three, 0)
		self.pi.set_servo_pulsewidth(self.motor_four, 0)
		self.pi.stop()
		os.system ("sudo killall pigpiod")
		
		
	# Shutdown
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
			print "Calibration Complete"
			time.sleep(1)
		
	def __init__(self):
			
		self.rate = rospy.Rate(90)
		self.flight_mode = False
		
		# GPIO pin number and wire color
		self.motor_one = 6 # yellow wire
		self.motor_two = 13 # orange
		self.motor_three = 19 # white
		self.motor_four = 26 # blue
		self.max_val = 2000 #max PWM
		self.min_val = 700  #min PWM
		self.pi = pigpio.pi()
		
		# Subscribe to interface and goal publishers
		rospy.Subscriber("interface_flags", Interface, self.interface_cb)
		# Subscribe to spin rates publisher
		rospy.Subscriber("cmd_spin", SpinRates, self.control_cb)
		
		while not rospy.is_shutdown():
			self.rate.sleep()
		
if __name__ == '__main__':
	# Initialize node
	rospy.init_node('motor_control')

	try:
		motor_control = MotorControl()
	except rospy.ROSInterruptException:
		pass


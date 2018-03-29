import os
import pigpio
import time

from esc import Esc

class MotorController:
	max_val = 2000 #max PWM
	min_val = 700  #min PWM
    
	# Initialize motors
	def motors_start(self):
		for esc in self.esc_list:
			self.pi.set_servo_pulsewidth(esc.location, 0)
		
	# Set all motors to min_val
	def motors_min(self):
		for esc in self.esc_list:
			self.pi.set_servo_pulsewidth(esc.location, MotorController.min_val)
		
	# Set all motors to max_val
	def motors_max(self):
		for esc in self.esc_list:
			self.pi.set_servo_pulsewidth(esc.location, MotorController.max_val)
		
	# Arming procedure of an ESC
	def motors_arm(self): 
		print('Arming Motors - Should hear two beeps')
		self.motors_max()
		time.sleep(1.5)
		self.motors_min()
		time.sleep(1)
		print('Motors Armed')
	
	# Update the PWM of a motor
	def set_pwm(self, esc, pwm): 
		max_cur = 1500
		min_cur = 1100
		
		# TODO: add call to spin_to_pwm
		if pwm > max_cur:
			pwm = max_cur
		if pwm < min_cur:
			pwm = min_cur
			  
		self.pi.set_servo_pulsewidth(esc.location, pwm)
    
    # Stop all motors
	def motors_stop(self): 
		for esc in self.esc_list:
			self.pi.set_servo_pulsewidth(esc.location, 0)
			
		self.pi.stop()
		os.system ("sudo killall pigpiod")
		print "Motors stopped"
		
	def __init__(self):
		self.esc_one = Esc('front left', 6, 'yellow wire')
		self.esc_two = Esc('front right', 13, 'orange wire')
		self.esc_three = Esc('back left', 19, 'white wire')
		self.esc_four = Esc('back right', 26, 'blue wire')
		self.esc_list = [self.esc_one, self.esc_two, self.esc_three, self.esc_four]
		self.pi = pigpio.pi()
		
		

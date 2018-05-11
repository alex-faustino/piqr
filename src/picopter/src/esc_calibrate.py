import os
import pigpio
import time

from esc import Esc

# launch GPIO
os.system ("sudo pigpiod")
time.sleep(1.5)

class ESCCalibrate:
	# Initialize motors
	def motors_start(self):
		for esc in self.esc_list:
			self.pi.set_servo_pulsewidth(esc.location, 0)
		
	# Set all motors to min_val
	def motors_min(self):
		for esc in self.esc_list:
			self.pi.set_servo_pulsewidth(esc.location, self.min_val)
		
	# Set all motors to max_val
	def motors_max(self):
		for esc in self.esc_list:
			self.pi.set_servo_pulsewidth(esc.location, self.max_val)
	
	# Stop all motors
	def motors_stop(self): 
		for esc in self.esc_list:
			self.pi.set_servo_pulsewidth(esc.location, 0)
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
		self.esc_one = Esc('front right', 6, 'yellow wire')
		self.esc_two = Esc('back right', 13, 'orange wire')
		self.esc_three = Esc('front left', 19, 'white wire')
		self.esc_four = Esc('back left', 26, 'blue wire')
		self.esc_list = [self.esc_one, self.esc_two, self.esc_three, self.esc_four]
		self.max_val = 2000 #max PWM
		self.min_val = 700  #min PWM
		self.pi = pigpio.pi()
		
		self.motors_calibrate()

if __name__ == '__main__':
	esc_calibrate = ESCCalibrate()

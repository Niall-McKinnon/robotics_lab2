# Import problem 2 solution as well as numpy and math
import p2_sol as p2
import math
import numpy as np

# Define a function for each transformation problem:

def H_1():
	# A translation of 2.5 units along the current x-axis
	Tx = p2.trans_x(2.5)
	
	# A translation of 0.5 units along the current z-axis
	Tz = p2.trans_z(0.5)
	
	# A translation of -1.5 units along the current y-axis
	Ty = p2.trans_y(-1.5)
	
	# Calculate transformation via current frame:
	# r1 = np.matmul(Tx, Tz)
	# r2 = np.matmul(r1, Ty)
	
	R = np.matmul(np.matmul(Tx, Tz), Ty)
	
	return R

def H_2():
	# A translation of 0.5 units along the current z-axis
	Tz = p2.trans_z(0.5)
	
	# A translation of 2.5 units along the current x-axis
	Tx = p2.trans_x(2.5)
	
	# A translation of -1.5 units along the current y-axis
	Ty = p2.trans_y(-1.5)
	
	# Calculate transformation via current frame:
	# r1 = np.matmul(Tz, Tx)
	# r2 = np.matmul(r1, Ty)
	
	# Combined calculations into one line:
	R = np.matmul(np.matmul(Tz, Tx), Ty)
	
	return R

def H_3():
	# A translation of 2.5 units along the current x-axis
	Tx = p2.trans_x(2.5)
	
	# A translation of 0.5 units along the current z-axis
	Tz = p2.trans_z(0.5)
	
	# A translation of -1.5 units along the current y-axis
	Ty = p2.trans_y(-1.5)
	
	# Calculate transformation via fixed frame (opposite order from H_1):
	# r1 = np.matmul(Tz, Tx)
	# r2 = np.matmul(Ty, r1)
	
	# Combined calculations into one line:
	R = np.matmul(Ty, np.matmul(Tz, Tx))
	
	return R

def H_4():
	# A translation of 0.5 units along the current z-axis
	Tz = p2.trans_z(0.5)
	
	# A translation of 2.5 units along the current x-axis
	Tx = p2.trans_x(2.5)
	
	# A translation of -1.5 units along the current y-axis
	Ty = p2.trans_y(-1.5)
	
	# Calculate transformation via fixed frame (opposite order from H_2):
	# r1 = np.matmul(Tx, Tz)
	# r2 = np.matmul(Ty, r1)
	
	# Combined calculations into one line:
	R = np.matmul(Ty, np.matmul(Tx, Tz))
	
	return R
	
def H_5():
	# Define angle:
	theta = math.pi / 2
	
	# A rotation by angle pi/2 about the current x-axis
	Rx = p2.rot_x(theta)
	
	# A translation of 3 units along the current x-axis
	Tx = p2.trans_x(3)
	
	# A translation of -3 units along the current z-axis
	Tz = p2.trans_z(-3)
	
	# A rotation by angle  ―pi/2 about the current z-axis
	Rz = p2.rot_z(-theta)
	
	# Calculate transformation via current frame:
	# r1 = np.matmul(Rx, Tx)
	# r2 = np.matmul(r1, Tz)
	# r3 = np.matmul(r2, Rz)
	
	# Combined calculations into one line:
	R = np.matmul(np.matmul(np.matmul(Rx, Tx), Tz), Rz)
	
	return R

if __name__ == '__main__':

	# Set output format
	np.set_printoptions(precision = 2, suppress = True)
	
	# Call problem functions and print results:
	
	print('===== Problem 3: =====')
	
	print('H_1 results:\n', H_1(), '\n')
	
	print('H_2 results:\n', H_2(), '\n')

	print('H_3 results:\n', H_3(), '\n')
	
	print('H_4 results:\n', H_4(), '\n')
	
	print('H_5 results:\n', H_5(), '\n')

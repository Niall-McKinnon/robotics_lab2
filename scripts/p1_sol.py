# Import rbm module from class as well as numpy and math
import rbm
import math
import numpy as np

if __name__ == '__main__':
	
	# Define angles:
	psi = math.pi / 2
	theta = math.pi / 2
	phi = math.pi / 2
	
	# format output:
	np.set_printoptions(precision = 2, suppress = True)
	
	# Define 3D vector (using example from class):
	v0 = rbm.vec(0, 1, 1)
	
	# Define rotation about x-axis:
	Rx = rbm.rot_x(psi)
	
	# Define rotation about y-axis:
	Ry = rbm.rot_y(theta)
	
	# Define rotation about z-axis:
	Rz = rbm.rot_z(phi)
	
	# Rotate about fixed frame:
	# Multiply x and y first, then z
	R = np.matmul((np.matmul(Rx, Ry)), Rz)
	
	# Calculate results with dot product:
	result = R.dot(v0)
	
	print('The results are:\n', result)
	
	
	

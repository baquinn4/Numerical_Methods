
import numpy as np 
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

# Given n by n matrix

A_initial = np.array([[2,1,-1,2],[4,4,1,3],[-6,-1,10,10],[-2,1,8,4]], dtype=float)

# Given column vector

b = np.array([[2,4,-5,1]],dtype=float).T

# Create augmented matrix

AM = np.append(A_initial,b,1)

# number of rows/columns

num_rows=AM.shape[0]
num_cols=AM.shape[1]

# storage for solutions

x = np.array([[0,0,0,0]],dtype=float).T


def GaussElim():
	#elimination process
	for i in range(num_cols-1):
		for j in range(i+1,num_rows):
			AM[j,:] =-(AM[j,i]/AM[i,i])*AM[i,:]+AM[j,:]
			
	#backward substitution
	for i in range(num_rows-1,-1,-1):
		x[i]=(AM[i,-1]-AM[i,0:num_cols-1]@x)/AM[i,i]


def printout():
	print("\nAx = b\n")
	print("A = ")
	print(A_initial)
	print("\nx = ")
	print(x)
	print("\nb = ")
	print(b)
	

GaussElim()
printout()
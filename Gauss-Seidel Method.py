
import numpy as np
import scipy
import pandas as pd

df = pd.DataFrame(columns = ["k","x1","x2","x3","x4","x5","x6"])


np.set_printoptions(formatter={'float': lambda x: "{0:0.4f}".format(x)})

# Num of iterations, assuming 5 from given output on project pdfS

NUM_ITERATIONS = 7

# Constructed A matrix from given system of linear equations

A = np.array([[4,-1,0,1,0,0],
			  [-1,4,-1,0,1,0],
			  [0,-1,4,0,0,-1],
			  [-1,0,0,4,-1,0],
			  [0,-1,0,-1,4,-1],
			  [0,0,-1,0,-1,4]], dtype=float)

# Constructed b column vector from given system of linear equations

b = np.array([0,5,0,6,-2,6], dtype=float).T

# initial guess of solution set, column vector x , for this example all intitial guesses set to zero

x_initial = np.zeros_like(b)

# variable for difference in euclidean norm of current and past estimate

euclid_norm_diff = np.zeros((NUM_ITERATIONS,1))

for count in range(0,NUM_ITERATIONS):
	x_update = np.zeros_like(x_initial)
	df = df.append({'k' : count, 'x1' : x_initial[0], 'x2' : x_initial[1], 'x3' : x_initial[2], 'x4' : x_initial[3], 'x5' : x_initial[4], 'x6' : x_initial[5]}, ignore_index=True)
	
	for i in range(len(A)):
		s1 = np.dot(A[i, :i],x_initial[:i])
		s2 = np.dot(A[i, i + 1 :], x_initial[i + 1 :])
		x_update[i] = (b[i] - s1 - s2) / A[i,i]
	if count != 0:
		euclid_norm_diff[count] = np.linalg.norm(x_update) - np.linalg.norm(x_initial)
	
	if np.allclose(x_initial,x_update,rtol=1e-4):
		break

	x_initial = x_update
df['Diff'] = euclid_norm_diff
print("\n\n")
print(df.to_string())

print("\n Ax = b \n")
print("\n A =")
print(A)
print("\n x =")
print(x_initial.T)
print("\n b =")
print(b.T)


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt



x0 = 0
y0 = 1
n = 4
h = 0.25

x = [0.0,0.25,0.50,0.75]
y = np.zeros(n)

y[0] = y0



for i in range(1,n):
	y[i] = y[i-1] + h * (x[i-1]*y[i-1] + (4*x[i-1]/y[i-1]))
	


print("h  ","  x","  yh(x)")
for i in range(n):
	print(h,x[i],y[i])


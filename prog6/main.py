
import pandas as pd 

import math



#This program approximates the derivative of sin(x) at x = (2/3)*pi with varying delta-x values using the FDF,BDF,LB,UC methods.
# Every method returns a double, all the data is stored in a pandas dataframe.
#
# @author Bradley Quinn
# @since 10/30/20

h_values = [0.1,0.5,0.025,0.0125,0.00625]
x0 = (2.0/3.0) * math.pi

#This progr

def FDF(h):
	f_prime = (math.sin(x0 + h) - (math.sin(x0)))/h
	return f_prime

def BDF(h):
	f_prime = ((math.sin(x0)) - (math.sin(x0 - h)))/h
	return f_prime
		
def LB(h):
	f_prime = ((math.sin(x0 + h)) - (math.sin(x0 - h))) / (2.0*h)
	return f_prime

def UC(h):
	f_prime = ((math.sin(x0 + h)) - (2*math.sin(x0)) + (math.sin(x0 - h))) / (math.pow(h,2))
	return f_prime

def main():
	df = pd.DataFrame(columns = ["h","FDF","BDF","LB","UC"])
	values_row = []
	for h in h_values:
		values_row.append(h)
		values_row.append(FDF(h))
		values_row.append(BDF(h))
		values_row.append(LB(h))
		values_row.append(UC(h))
		values_serie = pd.Series(values_row, index = df.columns)
		df = df.append(values_serie, ignore_index=True)
		values_row = []
	print(df.to_string())

main()

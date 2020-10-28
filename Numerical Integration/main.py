
import math

# This program numerically(integrates) approximates the given integral f(x) = ln(x) on [1,3] with n = 512 using
# both the Trapezoidal Rule and Simpsons Rule
#
# CSC 2262 Programming Project 5
#
# @author Bradley Quinn
# @since 10/28/20


# Given final values
UPPER_BOUND = 3
LOWER_BOUND = 1
SUBINTERVALS = 512

#change in x, same value for either rule, (b-a)/n
D_X = (UPPER_BOUND - LOWER_BOUND)/SUBINTERVALS

# This method creates our function f(x) = ln(x)
#
# Method: f(x)
#
# Return Type: double
#
# Parameters: some value xi, where xi is := LOWERBOUND(a) + i*D_X
#
# @author Bradley Quinn
# @since 10/28/20
def f(x):
	return math.log(x)

# Trapezoidal rule for numerically approximating the integral given, f(x) = ln(x) on [1,3] with n = 512
#
# Method: TrapezoidalRule()
#
# Return Type: double
#
# @author Bradley Quinn 
# @since 10/28/30
def TrapezoidalRule():
	sum_xi = 0
	for i in range(0,SUBINTERVALS + 1):
		xi = LOWER_BOUND + i*D_X
		if i == 0 or i == SUBINTERVALS - 1:
			sum_xi = sum_xi + f(xi)
		else:
			sum_xi = sum_xi + 2*f(xi)

	return (D_X/2) * sum_xi


# Simpsons rule for numerically approximating the integral given, f(x) = ln(x) on [1,3] with n = 512
# Only applicable when n is even
#
# Method: SimpsonsRule()
#
# Return Type: double
#
# @author Bradley Quinn
# @since 10/28/20
def SimpsonsRule():
	sum_xi = 0
	for i in range(0,SUBINTERVALS + 1):
		xi = LOWER_BOUND + i*D_X
		if i == 0 or i == SUBINTERVALS - 1:
			sum_xi = sum_xi + f(xi)
		elif isOdd(i):
			sum_xi = sum_xi + 4*f(xi)
		else:
			sum_xi = sum_xi + 2*f(xi)
	return (D_X/3) * sum_xi



# Method for determining if i is odd or even for conditional 4 or 2 scalar times f(xi) in Simpsons Rule
#
#
# Method: isOdd(x)
#
# Return Type: Boolean
#
# Parameters: some whole number integer
#
# @author Bradley Quinn
# @since 10/28/30
def isOdd(x):
	mod = x % 2
	if mod > 0:
		return True
	else:
		return False

t_approximation = TrapezoidalRule()
s_approximation = SimpsonsRule()

print("Trapezoidal Approximation: T512(f) = " + str(t_approximation))
print("Simpsons Approximation: T512(f) = " + str(s_approximation))
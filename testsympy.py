
from sympy import *
from sympy.abc import * 

# def user_input(exp):
# 	exp = raw_input('Enter User Input: ')
# 	print (exp)
# 	return exp


# def step_input(exp):
# 	exp = raw_input('Enter Step Output: ') 
# 	return exp

def check(exp_user, exp_step):
	# user = user_input(exp_user)
	# step = step_input(exp_step)
	return (simplify (exp_user - exp_step) == 0)


vers1 = sin(2*x)
print type (vers1)
vers2 = 2 *sin (x)*cos(x)
print type (vers2)

out = check(vers1,vers2)
print out 


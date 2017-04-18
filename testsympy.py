
from sympy import *
from sympy.abc import * 
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
transformations = (standard_transformations + (implicit_multiplication_application,))

import math


# def user_input(exp):
#  	exp = raw_input('Enter User Input: ')
#  	exp = parse_expr(exp, transformations = transformations)
#  	print exp
#  	return exp


# def step_input(exp):
# 	exp = raw_input('Enter Step Output: ')
# 	exp = parse_expr(exp, transformations = transformations)
# 	print exp
# 	return exp

# def check():
# 	user = user_input(exp)
# 	step = step_input(exp)
# 	return (simplify (user - step) == 0)


# out = check()
# print out 


user_input = parse_expr('a+b', transformations = transformations)
step_input = parse_expr('a', transformations = transformations)

def check(user_input, step_input):
	return (simplify (user_input - step_input) == 0)


out = check(user_input, step_input)
print out 




# print math.sin 90


# print math.sin(math.radians(90))





#p rint ((a+b)**2).__eval()__ 

# .__eq__(b**2+a**2+2*a*b)
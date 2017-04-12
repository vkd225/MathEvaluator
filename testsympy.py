
from sympy import *
from sympy.abc import * 
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
transformations = (standard_transformations + (implicit_multiplication_application,))

import math


def user_input(exp):
 	exp = raw_input('Enter User Input: ')
 	exp = parse_expr(exp, transformations = transformations)
 	print exp
 	return exp


def step_input(exp):
	exp = raw_input('Enter Step Output: ')
	exp = parse_expr(exp, transformations = transformations)
	print exp
	return exp

def check():
	user = user_input(exp)
	step = step_input(exp)
	return (simplify (user - step) == 0)


out = check()
print out 

# print math.sin 90


aa= parse_expr("2x", transformations = transformations)
# print aa

print math.sin(math.radians(90))


# ver1 = sin(x)**2 + cos(x)**2
# ver2 = 1
# print simplify(ver1-ver2) == 0
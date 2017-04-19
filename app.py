from sympy import *
from sympy.abc import * 
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
transformations = (standard_transformations + (implicit_multiplication_application,))

import math


from flask import Flask, render_template, json, request, send_file
app = Flask(__name__)

@app.route("/home")
def main():
    return render_template ('index.html')


@app.route('/')
def step_evaluate():
	return render_template ('step_evaluate.html')

@app.route('/', methods = ['GET','POST'])
def step_evaluate_post():

	# def user_input(exp):
	#  	# exp = raw_input('Enter User Input: ')
	#  	exp = parse_expr(exp, transformations = transformations)
	#  	# print exp
	#  	return exp


	# def step_input(exp):
	# 	# exp = raw_input('Enter Step Output: ')
	# 	exp = parse_expr(exp, transformations = transformations)
	# 	# print exp
	# 	return exp

	def check(user_input, step_input):
		# user = user_input(exp)
		# step = step_input(exp)
		return (simplify (user_input - step_input) == 0)


	user_input = request.form['user_input']
	user_input = parse_expr(user_input, transformations = transformations)
	step_input = request.form['step_input']
	step_input = parse_expr(step_input, transformations = transformations)

	out = check(user_input, step_input)
	
	if (out == True):
		filename = 'success.jpg'
		# return 'Success'
	else:
		filename = 'fail.jpg'
		#return 'fail'
	
	# return filename
	# return send_file(filename, mimetype = 'image/jpeg')
	return app.send_static_file (filename)

if __name__ == "__main__":
	app.debug = True
	app.run()


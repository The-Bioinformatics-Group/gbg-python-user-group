#!/usr/bin/python

# Example of functions that returns a value, prints or don't return a value.

# 1. Define the functions 

# Do the calcultation but return nothing.
def return_nothing(x):
	y = x + 1

# Do the calculation print the value but return nothing.
def print_no_return(x):
	x = x + 1
	print x

# Do the calculation and return the value.
def return_value(x, i):
	x = x + 1 + i
	return x

# 2. Run the code

x = 10
z = 42
j = 2

#return_nothing(x)
#print_no_return(x)
#return_value(z, j)

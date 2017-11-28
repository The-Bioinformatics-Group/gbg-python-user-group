#!/usr/bin/python

# Example of functions that returns a value, prints or don't return a value.

# 1. Define the functions 

# Do the calcultation but return nothing.
def return_nothing(x):
	y = x + 1

# Do the calculation print the value but return nothing.
def print_no_return(x):
	z = x + 1
	print "z =", z

# Do the calculation and return the value.
def return_value(x):
	w = x + 1
	return w

# 2. Run the code

x = 42

return_nothing(x)
print_no_return(x)
return_value(x)

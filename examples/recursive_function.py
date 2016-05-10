#!/usr/bin/python

# Example of a recursive function that will result in 
# a RuntimeError when the maximum recursion depth is exceeded.

# 1. Define the function
def recursive_count(n):
	print "n"
	n += 1
	recursive_count(n)

# 2. Run the program
recursive_count(1)

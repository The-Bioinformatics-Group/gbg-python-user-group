#!/usr/bin/python

# Example of a recursive function

# 1. Assign some values to some varables
n = 1
m = 100

# 1. Define the function
def recursive_count(n):
	print n
	n += 1
	if n < m:
		recursive_count(n)

# 2. Run the program
recursive_count(n)

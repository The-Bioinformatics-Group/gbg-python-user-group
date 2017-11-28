#!/usr/bin/python

# Example of a recursive function

# 1. Define the function
def recursive_count(n):
	if n > 0:
		print n
		recursive_count(n-1)

# 2. Run the program
recursive_count(10)

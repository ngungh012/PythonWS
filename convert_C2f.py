#!/usr/bin/env python

import sys

def celsius_to_fahr(temp_c):
	temp_f=temp_c*(9.0/5.0)+32
	return temp_f
try:
	cels=float(sys.argv[1])
	print(celsius_to_fahr(cels))
except:
	print("First argument must be a number! Try again")
	
 


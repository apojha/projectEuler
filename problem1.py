from math import *

def method():
	runningSum = 0;
	for x in range (0,1000):
		if x % 3 == 0 or x % 5 == 0:
			runningSum += x

	print runningSum

method()

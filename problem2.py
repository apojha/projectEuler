from math import *

def method():

	prevValue = 1
	value = 1

	runningSum = 0
	
	while (value < 4000000):
		temp = prevValue + value;
		prevValue = value;
		value = temp;
		if prevValue % 2 == 0:
			runningSum += prevValue
		
	print runningSum

method()

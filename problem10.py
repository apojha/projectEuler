from math import *
from functions import *

def method(ceiling):
	currentPrime = 2
	runningSum = 0
	while(currentPrime < ceiling):
		runningSum += currentPrime
		currentPrime = nextPrime(currentPrime)

	print runningSum

method(2000000)

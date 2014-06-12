from math import *
from functions import *

def method(upperLimit):

	#for holding values 1 + 2 + ...
	vanillaSum=0

	#for holding values 1^2 + 2^2 + ...
	squareSum=0
	for i in range(upperLimit + 1):
		vanillaSum += i
		squareSum += i*i
	
	vanillaSumSquared = vanillaSum * vanillaSum

	print str(vanillaSumSquared - squareSum)


method(100)

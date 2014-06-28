from math import *
from functions import *

def method(target):
	for i in range(1, target):
		for j in range(i, target):
			k = target - i -j
			if isPythagoreanTriplet(i, j, k):
				print "Pyth triplet: " + str(i) + " " + str(j) + " " + str(k)
				print str(i * j * k)


def isPythagoreanTriplet(a, b, c):
	return (a*a + b*b == c*c)

method(1000)

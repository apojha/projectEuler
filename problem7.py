from math import *
from functions import *

def method(index):

	prime=1
	for i in range(index):	
		prime=nextPrime(prime)
	print prime	

method(10001)

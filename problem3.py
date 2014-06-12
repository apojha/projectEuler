from math import *
from functions import *

def method(n):
	return auxMethod(n, 2)	

def auxMethod(n, i):
	if (isPrime(n)):
		return n
	while(n % i == 0):
		n = n / i
	return auxMethod(n, nextPrime(i))

print method(600851475143)

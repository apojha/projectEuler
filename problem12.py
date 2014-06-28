from functions import *

def method(divisors):

	i = 1
	triangle = nthTriangleNumber(i)
	while(countDivisors(triangle)< divisors):
		i += 1
		triangle = nthTriangleNumber(i)

	return triangle

method(5)
		

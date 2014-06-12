from math import *
from functions import *

" method to find the minimum number that is evenly divisible by every number from 1 to 20
  begin by calculating the minimin which is the multiple of all the primes from 1 to 20
  minimum = * of all primes (1,20)
  we know that the final result must be a multiple of this minimum
  so try minimum * 1, minimum * 2 =, minimum * 3 etc until result found

  the toCheck list contains the non-prime values between 1 and 20 to check

  for further optimisation, i could have removed the j values from toCheck if they are in there"
def method(n):

	minimum = 1
	toCheck = []

	for i in range(1, n):
		if (isPrime(i)):
			minimum = minimum * i
		else:
			toCheck.append(i)
	toCheck.append(n)	

	j =1
	while(True):
		divisible = True
		value = minimum * j

		for i in toCheck:
			if not value % i == 0:
				divisible = False
				break

		if divisible:
			print value
			break
		j += 1


method(20)

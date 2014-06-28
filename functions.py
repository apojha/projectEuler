from math import *
from collections import Counter

def nextPrime(n):
	m = n + 1 
	while (not isPrime(m)):
		m+= 1
	return m;

def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True   

def isPalindrome(n):
	string_n = str(n)

	middle = len(string_n) / 2
	if not len(string_n) % 2 == 0: 
		middle += 1
	for i in range(0, middle):
		if not string_n[i] == string_n[len(string_n) - i - 1]:
			return False	
	
	return True


def nthTriangleNumber(n):
	return (n * (n+1))/2

def getDivisors(n):
	if n == 1: return [1]
	
	divisors = [1]
	root = int(sqrt(n))

	for i in range(2, root + 1):
		if n % i == 0: 
			divisors.append(i)
			divisors.append(n/i)

	if root * root == n: divisors.remove(root) #remove dupe

	divisors.append(n)
	return divisors

'''
returns a list of prime factors eg for n = 8 method returns[2,2,2]
'''

def getPrimeFactors(n):
	return getPrimeFactorsAux(n, 2, [])

def getPrimeFactorsAux(n, prime, resultsList):

	while (n % prime == 0):
		resultsList.append(prime)
		n = n / prime

	if n == 1: return resultsList
	else: return getPrimeFactorsAux(n, nextPrime(prime), resultsList)
	
def getPrimes(n):

	resultsList = []
	prime = 2

	while(n != 1):
		while (n%prime == 0):
			resultsList.append(prime)
			n = n/prime
		prime = nextPrime(prime)

	return resultsList
	
'''
prime factors - any combination of prime factors will give number of divisors

therefore use simple combinatorics to count divisors:

eg imagine n = 2^4 + 3^1
you can choose 0-4 twos and 0-1 threes => number of divisors = 5*2 = 10

this method returns an int
'''
def countDivisors(n):
	primeFactors = getPrimes(n)	
	counter = Counter(primeFactors)

	divisors = 1

	for prime in counter:
		divisors = divisors * (counter[prime] + 1)

	return divisors




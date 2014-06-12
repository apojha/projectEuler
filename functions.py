from math import *

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

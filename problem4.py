from math import *
from functions import *

def method(minimum, maximum):
	palindromes = []
	for i in range(maximum, minimum, -1):
		for j in range (i, minimum, -1):
			if isPalindrome(i*j):
				palindromes.append(i * j)

	print str(max(palindromes))

method(100, 1000)

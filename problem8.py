from math import *
from functions import *

"
given an input text file containing a long number (1000 digits) find the largest product you can
from 13 consecutive numbers

implementation details: I didnt want to repeatedly multiply the same numbers so i find the product of the first 12
then in the second for loop multiply by the 13th, check against max and divide by the 1st. 

This was a little problematic when dealing with 0s as the whole number has to be recalculated but oh well, it ran really fast. 

Of course, I could have done this with 2 nested for loops but this was more fun and didnt need to do as many multiplications
"
def method(index):
	# read from file 
	fileHandler = open('problem8.txt', 'r')
	numberAsString = fileHandler.read()

	# convert to eg ['9', '1', ... , '7' ]
	charArrayOfNumbersNoLineBreaks = [int(x) for x in list(numberAsString) if x != '\n']

	value = 1
	for i in range (index - 1):
		value = value * charArrayOfNumbersNoLineBreaks[i]

	maximum = 0
	for i in range(index - 1, len(charArrayOfNumbersNoLineBreaks)):

		value = value * charArrayOfNumbersNoLineBreaks[i]

		if (value > maximum):
			maximum = value
		
		firstInSequence = charArrayOfNumbersNoLineBreaks[i - index + 1]
		if (firstInSequence != 0):
			value = value / charArrayOfNumbersNoLineBreaks[i - index + 1]

		else:
			value = 1
			for j in range(i, i-index + 1, -1):
				value = value * charArrayOfNumbersNoLineBreaks[j]
				

	print maximum

method(13)

from math import *
from functions import *

def method(index):
	# read from file 
	fileHandler = open('problem11_test.txt', 'r')
	fileContents = fileHandler.read()

	lines = fileContents.split('\n')
	lines.pop()
	parsedLines = []

	for line in lines:
		parsedLines.append([int(val) for val in line.split(' ')])
	print parsedLines

	for rowIndex in range(len(parsedLines)):
		for columnIndex in range(len(parsedLines[0])):
			currentValue = parsedLines[rowIndex][columnIndex]

			#check up
			if rowIndex - index + 1>= 0:
				for i in range(rowIndex - index + 1, rowIndex):
					print str(i) + " " + str(columnIndex)
				#print str(rowIndex) + " " + str(columnIndex)
				
				
			
	# convert to eg ['9', '1', ... , '7' ]
	#blah = [int(x) for x in list(numberAsString) if x != '\n']

				


method(2)

#!/usr/bin/python

s = input("Enter a list of numbers: ").split()

def squareEach(nums):		# Returns a list of each number squared
	return [(int(i)**2) for i in nums]

def sumList(nums):			# Returns the sum of the numbers in the list
	sum = 0
	return [sum += int(i) for i in nums]
	
def toNumbers(strList):		# Converts a list of string nums into int nums
	return [int(i) for i in strList]
	
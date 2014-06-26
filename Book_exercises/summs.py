#!/usr/bin/python

def sumN(n):	#returns the sum of the first n natural numbers
	sum = 0
	for i in range(1, n+1):
		sum += i
	return sum

def sumNCubes(n):	#returns the sum of the cubes of the first n natural numbers
	sum = 0
	for i in range(1, n+1):
		sum += (i**3)
	return sum
	
def main():
	n = int(input("Enter a number to sum up! "))
	print("Your number summed by the first n numbers is {}".format(sumN(n)))
	print("Your number summed by the first n numbers cubed is {}".format(sumNCubes(n)))
		
if __name__ == "__main__":
	main()
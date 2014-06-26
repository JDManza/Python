#!/usr/bin/python
import math

def area_of_triangle(a, b, c):
	return math.sqrt((a+b+c) * (a + b - c) * (b + c - a) * (a + c - b)) / 4

def main():	
	a = float(input("Enter the length of a: "))
	b = float(input("Enter the length of b: "))
	c = float(input("Enter the length of c: "))

	print("The area of your triangle is {}".format(area_of_triangle(a, b, c)))
	
if __name__ == "__main__":
	main()
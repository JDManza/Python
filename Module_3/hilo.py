#!/usr/bin/python

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

if first > second:
	print("High/Low")
elif first == second:
	print("Equal")
elif first < second:
	print("Low/High")
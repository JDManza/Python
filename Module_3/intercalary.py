#!/usr/bin/python

year = int(input("Enter a year: "))

if year % 100 == 0:
	print("{} is not a leap year".format(year))
elif year % 4 == 0 or year % 400 == 0:
	print("{} is a leap year".format(year))
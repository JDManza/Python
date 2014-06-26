#!/usr/bin/python

wage = float(input("Enter hourly wage: ").strip('$'))
hrs = float(input("Enter hours worked: "))

if hrs > 40:
	ot = (hrs - 40) * (wage * 1.5)
	total = wage * hrs + ot
	print(total)
else:
	total = wage * hrs
	print(total)
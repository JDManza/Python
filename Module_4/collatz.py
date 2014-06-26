#!/usr/bin/python

num = int(input("Enter a number to collatzerate: "))
print(num)
while num != 1:
	if num % 2 == 0:
		num //= 2
	else:
		num = num * 3 + 1
	print(num)
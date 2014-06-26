#!/usr/bin/python

s = input("Enter a sentence to scan: ")
count = 0
for i in s.split():
	if i[0].lower() == i[-1].lower() and len(i) >= 2:
		count += 1
print("{} head-and-tail words".format(count))
#!/usr/bin/python

s = input("Enter a sentence for measurement: ")
print("{}\n{}".format(s.split(), [len(i) for i in s.split()]))
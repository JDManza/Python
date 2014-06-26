#!/usr/bin/python

s = input("Enter the phrase to acronymize: ")
print("".join([i[0].upper() for i in s.split()]))
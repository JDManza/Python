#!/usr/bin/python

req = input("Enter a sentence: ").split()
print("{0} {1} {2}".format(req[0], req[-1], len(req)))
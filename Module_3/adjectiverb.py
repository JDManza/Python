#!/usr/bin/python

word = input("Enter a word to adjectify or adverbate: ")

if len(word) >= 3 and word[-3:] != 'ing':
	print("{}".format(word + 'ing'))
elif word[-3:] == 'ing':
	print("{}".format(word + 'ly'))
else:
	print("{}".format(word))
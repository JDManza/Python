#!/usr/bin/python

word = input("Enter a word to obscure: ")
print(word[0]+word[1:].replace(word[0], '?'))
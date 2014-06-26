#!/usr/bin/python

s = input("Enter a list of your siblings: ").split()
t = input("Enter a list of your friends: ").split()

lst = [i for i in s if i not in t]
print("You are not friends with: {}".format(", ".join(lst)))
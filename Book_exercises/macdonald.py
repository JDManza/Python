#!/usr/bin/python

animals = {'duck': 'quack', 'cow': 'moo', 'platypus': '...', 'dragon': "HEY Y'ALL!!", 'japanese hornet': 'I WILL DESTROY YOU ALL'}
def song(animals):
	for i in animals:
		print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\nAnd on that farm he had a {0}, Ee-igh, Ee-igh, Oh!\nWith a {1}, {1} here and a {1}, {1} there.\nHere a {1}, there a {1}, everywhere a {1}, {1}.\nOld MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n".format(i, animals[i]))
		
song(animals)
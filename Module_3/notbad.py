#!/usr/bin/python

s = input("Enter a sentence to make good: ")

if 'bad' in s:
	if 'not' in s and 'bad' in s:
		s = s.replace(' not', '', 1).replace('bad', 'good', 1)
		if 'half-' in s:
			s = s.replace('half-', '', 1)
			print(s)
		else:
			print(s)
	elif s.index('not') > s.index('bad'):
		print(s)
elif 'not' in s and 'good' in s:
	print(s.replace(' not', '', 1).replace('good', 'bad', 1))
else:
	print(s)
	
# not_index = s.find('not')
# bad_index = s.find('bad')

# if -1 < not_index < bad_index
	# s = s[:not_index] + 'good' + s[bad_index+3:]
		
# print(s)
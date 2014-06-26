#!/usr/bin/python

s = input("Enter a string to deduplicate: ")
print("{0}".format(" ".join(set((s.lower()).split()))))

# s = input("Enter a string to deduplicate: ")
# no_dups = " ".join(set((s.lower()).split()))
# in_order = []
# s = s.split()
# print(s)
# no_dups = no_dups.split()
# print(no_dups)
# for i in s:
	# for j in no_dups:
		# if s[j] != no_dups[j]:
			# in_order.append(s[j])
		# else:
			# continue
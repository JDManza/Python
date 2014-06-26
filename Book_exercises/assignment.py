#!/usr/bin/python


def main():
	for i in reversed(range(2, 100)):
		print("{0} bottles of beer on the wall!\n{0} bottles of beer!\ntake one down pass it round\n{1} bottles of beer on the wall!\n".format(i, i-1))
	print("1 bottle of beer on the wall\n1 bottle of beer\ntake one down pass it round\nNo more bottles of beer on the wall!\n".format(i, i-1))
		
if __name__ == "__main__":
	main()
#!/usr/bin/python

def fibo(n):
	if n <= 1:
		return n
	else:
		return fibo(n-1) + fibo(n-2)
		
def main():
	n = int(input("Enter a number to fibo! "))
	print("Your number is {}".format(fibo(n)))
	
if __name__ == "__main__":
	main()
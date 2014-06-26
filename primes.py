#!/usr/bin/python

def is_prime(n):
	if n <= 0:
		return False
	elif n == 1:
		return True
	for num in range(2, n-1):
		if (n % num == 0):
			return False
	return True
	
def main():
	rng = int(raw_input("Enter a range of numbers to determine primes: "))
	yield [i for i in range(rng) if is_prime(i)]
	
if __name__ == "__main__":
	main()
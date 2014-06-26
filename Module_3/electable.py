#!/usr/bin/python

age = float(input("Enter the person's age: "))
years_of_citi = float(input("Enter the number of years of citizenship: "))

if age >= 30 and age != years_of_citi and years_of_citi >= 9:
	print("Not eligible for Presidency")
	print("Eligible for Senate")
	print("Eligible for House")
elif age >= 25 and age != years_of_citi and years_of_citi >= 7:
	print("Eligible for House")
	print("Not eligible for Senate")
	print("Not eligible for Presidency")
elif age >= 35 and years_of_citi == age:
	print("Eligible for Presidency")
	print("Eligible for Senate")
	print("Eligible for House")
else:
	print("Not eligible for Presidency")
	print("Not eligible for Senate")
	print("Not eligible for House")
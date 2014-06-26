#!/usr/bin/python

lbs = float(input("Enter the weight in pounds: "))
height = float(input("Enter the height in inches: "))

bmi = (lbs / 2.20462) / ((height * 0.0254) ** 2)

if bmi >= 30:
	print("{}\n{}".format(bmi, "Obese"))
elif bmi >= 25 and bmi < 30:
	print("{}\n{}".format(bmi, "Overweight"))
elif bmi >= 18.5 and bmi < 25:
	print("{}\n{}".format(bmi, "Normal"))
else:
	print("{}\n{}".format(bmi, "Underweight"))
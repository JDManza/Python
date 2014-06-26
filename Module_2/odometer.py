print("Welcome to Odometer!")
init = float(input("Enter the initial odometer reading: "))
fin = float(input("Enter the final odometer reading: "))
num_gals = float(input("Enter the number of gallons used: "))
cpg = float(input("Enter the cost per gallon: "))

miles_driven = fin - init
mpg = miles_driven / num_gals
cpm = cpg / mpg

print("Total miles: %5.2f" % miles_driven)
print("mpg: %5.2f" % mpg)
print("cpm: %5.2f" % cpm)
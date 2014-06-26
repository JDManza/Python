fahr = float(input("Enter the temperature in degrees Fahrenheit: "))
cels = 5/9 * (fahr - 32)
kel = cels + 273.5
deg = u"\u00b0"
print("%0.1fF%s = %0.1fC%s = %0.1fK%s" % (fahr, deg, cels, deg, kel, deg))
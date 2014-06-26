import math

r = float(input("Enter the radius of the sphere: "))
v = 4 / 3 * math.pi * (r ** 3)
sa = 4 * math.pi * (r ** 2)
print("Volume =       %8.2f" % v)
print("Surface Area = %8.2f" % sa)
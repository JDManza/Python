import math

a = float(input("Enter side a length: "))
b = float(input("Enter side b length: "))
c = float(input("Enter side a length: "))

perimeter = a + b + c
s = perimeter / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("Perimeter = %8.3f" % perimeter)
print("Area =      %8.3f" % area)
#!/usr/bin/python

def sphereArea(r):
	area = 4 * r ** 2
	return area
	
def sphereVolume(r):
	vol = (4/3) * r ** 3
	return vol
	
def main():
	rad = float(input("Enter the radius of your sphere: "))
	
	print("The area of your sphere is {}.".format(sphereArea(rad)))
	print("The volume of your sphere is {}.".format(sphereVolume(rad)))
	
if __name__ == "__main__":
	main()
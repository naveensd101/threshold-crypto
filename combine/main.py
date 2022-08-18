#!/bin/python3
from scipy.interpolate import lagrange
from math import floor
def main():
	print("Enter number of keys: ", end="")
	number_of_keys = int(input())
	x = []
	y = []
	print("Enter the key pairs (i, q(i)) order with spaces:")
	for _ in range(number_of_keys):
		_x,_y= input().split()
		_x = int(_x)
		_y = int(_y)
		x.append(_x)
		y.append(_y)

	poly = lagrange(x, y)
	print(f"The secret is : {floor(poly(0))}")

main()

class Data:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def interpolate(f: list, xi: int, n: int) -> float:

	result = 0.0
	for i in range(n):

		term = f[i].y
		for j in range(n):
			if j != i:
				term = term * (xi - f[j].x) / (f[i].x - f[j].x)

		result += term

	return result

if __name__ == "__main__":
	print("Enter number of keys")
	n = int(input())
	f = []
	#2 <value at 2>
	#1 <value at 1>
	for _ in range(n):
		a,b = input().split()
		a = int(a)
		b = int(b)
		f.append(Data(a,b))

	# Using the interpolate function to obtain a data point
	# corresponding to x=3
	print("Value is:", interpolate(f, 0, n))

# This code is contributed by
# sanjeev2552



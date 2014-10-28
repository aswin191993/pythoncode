def square(i):
	print i*i

def map(square,y):
	[square(i) for i in range(1,5)]

map(square,range(5))

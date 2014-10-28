def even(i):
	if i%2==0:
		print i

def filter(square,y):
	[even(i) for i in y]

filter(even,range(10))

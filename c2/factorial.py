x=range(6)
y=x[::-1]
k=y[:-1]

def factorial(k):
	product=1
	for i in k:
		product=(product*i)
	return product

print factorial(k)


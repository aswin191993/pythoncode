x=[1,2,3,4,6,7,8]

def cumulative_product(x):
	product=1
	a=[]
	for i in x:
		product=(product*i)
		a.append(product)
	print a

print x
cumulative_product(x)


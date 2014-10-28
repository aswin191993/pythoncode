x=[1,2,3,4,5,6,7]
y=3
def group(x,y):
	l=(len(x))/(y)
	j=range(l+2)
	n=[]
	for i in j: 
		n.append(x[(i*y)-y:(y*i)])
	print n

group(x,y)

x=['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']

def extsort(x):
	x.sort(key= lambda x: len(x))
	print x

extsort(x)

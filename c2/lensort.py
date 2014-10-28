y=['python','perl','java','c','haskell','ruby']

def lensort(y):
	s=[]
	y.sort(key=lambda x: len(x))
	print y

lensort(y)


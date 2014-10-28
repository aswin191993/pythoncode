x=[1,1,1,1,3,4,4,5,6]

def dups(x):
	y=len(x)
	p=range(y)
	a=[]
	k=0
	s=1
	for i in x:
		if s<y:
			if i==x[s] & i not in a:
				a.append(i)
		s+=1
	print a
				
dups(x)

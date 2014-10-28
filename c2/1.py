x=[0,1,[2]]
x[2][0]=3 
print x //error

x[2].append(4)
print x //output: [0,1,[2,4]]

x[2]=2
print x //output: [0,1,2]


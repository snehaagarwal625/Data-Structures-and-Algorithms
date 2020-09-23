a=[(0,1,2,3),(0,1,2,3,4)]
b=[0,1]
c=[]
for i in range(len(a)):
    c.extend(list(map(lambda x: (b[i],x), a[i])))
print(c)
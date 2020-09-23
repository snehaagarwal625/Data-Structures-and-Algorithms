val=input("Enter the string to reverse:")
t = list(val)
for i in range(0,int(len(t)/2)):
    t[i], t[len(t)-1-i] = t[len(t)-1-i], t[i]
t=''.join(t)
print(t)
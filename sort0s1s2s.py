A = [1,2,0,0,2,1,1,2,0,0,2,1,1]
count0=0
count1=0
count2=0

for a in A:
    if a == 0:
        count0 = count0+1
    if a == 1:
        count1 = count1+1
    if a == 2:
        count2 = count2+1
for i in range(0, count0):
     A[i] = 0
for i in range(count0, (count0+count1)):
     A[i] = 1
for i in range((count0+count1), len(A)):
     A[i] = 2
 

for i in A:
    print(i)

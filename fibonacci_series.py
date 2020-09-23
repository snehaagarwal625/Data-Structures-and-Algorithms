num = int(input("enter the limit: "))

list1=[None]*(num)
list1[0] = 0
list1[1] = 1
def fibo(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        c = fibo(num-2)+fibo(num-1)
        if(list1[num-1] == None):
            list1[num-1]=c
        return c

       # 2 - [0,1]
       # 3 - [0,1,1]
       # 4 - [0,1,1,2]
    
    
print(fibo(num))
print(list1) 


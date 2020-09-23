num = int(input("enter the limit: "))

list1=[None]*(num+1)

def fibo(num):
    if(list1[num]!=None):
        return list1[num]
    if num == 1:
        result =  0
    elif num == 2:
        result = 1
    else:
        result =  fibo(num-2)+fibo(num-1)
    list1[num] = result
    return result
                 
print(fibo(num))



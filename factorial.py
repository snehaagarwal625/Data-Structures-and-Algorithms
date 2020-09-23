val = int(input("enter the value whose factorial needs to be calculated:"))
# def factorial(val):
#     if(val==1):
#         return 1 
#     return val*factorial(val-1)
# print(factorial(val))


# memoize
# memo = [None]*(val+1)
# def factorial(n, memo):
#     if(memo[n]!=None):
#         return memo[n]
#     if(n==1):
#         result = 1 
#     else:
#         result = n*factorial((n-1), memo)
#     memo[n] = result
#     return result
# print(factorial(val, memo))


# bottom-up approach
def factorial(n):
    memo = [None]*(val+1)
    if(memo[n]!=None):
        return memo[n]
    memo[1]=1
    for i in range(2, n+1):
        memo[i] = i*memo[i-1]
    return memo[n]
print(factorial(val))

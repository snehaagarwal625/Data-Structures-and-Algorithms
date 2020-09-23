def reverse(num):
    rev = 0
    while(num>0):
        d = num % 10
        rev = rev * 10 + d
        num = num // 10
    return rev

def isPallindrome(n):
    return (n == reverse(n))

val=int(input("Enter the number to check if it is a pallindrome:"))
print(isPallindrome(val))
# val=input("Enter the string to check if it is a pallindrome:")
# t = list(val)
# for i in range(0,int(len(t)/2)):
#     t[i], t[len(t)-1-i] = t[len(t)-1-i], t[i]
# t=''.join(t)
# if(val == t):
#     print("the string is a pallindrome")
# else:
#     print("the string is not a pallindrome")
# print(t)

val=input("Enter the string to check if it is a pallindrome:")
for i in range(0,int(len(val)/2)):
    if(val[i]==val[len(val)-1-i]):
        continue
    else:
        print("the string is not a pallindrome")
        exit(0)
print("the string is a pallindrome")


val=input("Enter the string to check if it is a pallindrome:")
for i in range(0,int(len(val)/2)):
    if(val[i]!=val[len(val)-1-i]):
        print("the string is not a pallindrome")
        exit(0)
print("the string is a pallindrome")
n=int(input("enter the num:"))
a=n
rev=0
while (n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
# print("a=",a)
# print("rev=",rev)
if a==rev:
    print(a,"is palindrome.")
else:
    print(a,"not a palindrome")

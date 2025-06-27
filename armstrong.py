n=int(input("enter number:"))
arm=0
a=n
len=len(str(n))
while(n>0):
    rem=n%10
    arm+=rem**len
    n=n//10
if (a==arm):
    print(a,"is armstrong.")
else:
    print(a,"not an armstrong.")
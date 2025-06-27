a=int(input("enter the starting position:"))
b=int(input("enter the ending position:"))
odd=0
even=0
for i in range(a,b+1):
    if i%2==0:
        even+=1
    else:
        odd+=1
print(" count of even number:",even)
print(" count of odd number:",odd)

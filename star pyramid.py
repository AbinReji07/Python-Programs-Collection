'''

i=row=3
j=star
k=space

i=0,1,2,3
j=1,2,3,4
k=3,2,1,0
'''
row=int(input("enter the num of row:"))
for i in range(row):
    for k in range(0,row-1-i):
        print(" ",end=" ")
    for j in range(0,i+1):
        print("*  ",end=" ")
    print(" ")

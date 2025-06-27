'''
i=0,j=3
i=1,j=2
'''
row=int(input("enter the number of rows:"))
for i in range(0,row):
    for j in range(0,row-i):
        print("*",end=" ")
    print(" ")

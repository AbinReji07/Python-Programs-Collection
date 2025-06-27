'''
1
1 2
1 2 3


i=row     0,1,2
j=number
1
'''
row=int(input("enter num of row:"))
for i in range(0,row):
    for j in range(0,i+1):
        print(j+1,end="")
    print("")


#i=0,1,2
#j=1,2,3
'''
row=int(input("enter the number of rows:"))
for i in range(row):
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")

1
1 2
1 2 3
1 2 3 4'''
#i=0,1,2,3
#j=
'''
row=int(input("enter the number of rows:"))
for i in range(0,row):
    for j in range(0,i+1):
        print(j+1,end="")
    print(" ")
 '''   
1234
123
12
1
row=int(input("enter number row"))
for i in range(0,row):
    for j in range(0,row-i):
        print(j+1,end=" ")
    print(" ")

    
        

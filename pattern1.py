i = 0
j = 0
n =  int(input("Enter n num"))
for i in range(0,n):
    for j in range(0,n-1-i):
        print(" ",end="")
    for j in range(0,(2*i)+1):
        print("*",end="")
    print()
rowsize=int(input("Enter the number of rows:"))
for i in range (1,rowsize+1):
    for j in range (1,rowsize-i+1):
        print(end=" ")
    for k in range (2*i-1):
        print("*",end="")
    print()
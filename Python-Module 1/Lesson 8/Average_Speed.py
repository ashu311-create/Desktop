a=int(input("Enter a value:"))
b=int(input("Enter the 2nd value:"))
c=int(input("Enter the third value:"))
avg=a+b+c/3
print("Average=",avg)
if avg>a and avg>b and avg>c:
    print ("Average is greater than all values")
elif avg>a and avg>b:
    print("Average is greater than the 1st and 2nd numbers")
elif avg>0 and avg>c:
    print("Average is greater than the 1st and 3rd numbers")
elif avg>b and avg>c:
    print("Average is greater than the 2nd and 3rd numbers")
elif avg>a:
    print("Average is greater than the 1st number")
elif avg>b:
    print("Average is greater than the 2nd number")
elif avg>c:
    print("Average is greater than the 3rd number")
else:
    print("Wrong input!")
num=int(input("Please enter the number you have as your base:"))
exponent=int(input("Enter the exponent/power of the base:"))
result=1
for i in range(exponent):
    result=result*num
print("When the base is raised to the power that is give, the answer is",result)
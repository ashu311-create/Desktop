height=float(input("Enter your height in cm"))
weight=float(input("Enter your weight in kg"))
BMI=weight/(height/100)**2
print("Your BMI is",BMI)
if BMI<=19.4:
    print("You are underweight")
elif BMI<=24.4:
    print("You are healthy")
elif BMI<=29.5:
    print("You are overweight")
elif BMI<=34.5:
    print("You are severely overweight")
elif BMI<=39.5:
    print("You are obese")
else:
    print("You are severely obeses")
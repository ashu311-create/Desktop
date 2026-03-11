try:
    age=int(input("Enter your age:"))
    if age > 100:
        raise ValueError
except ValueError:
    print ("Enter a valid age.")
except:
    print("Invalid")
else:
    if age%2==0:
        print("Even")
    else:
        print("Odd")
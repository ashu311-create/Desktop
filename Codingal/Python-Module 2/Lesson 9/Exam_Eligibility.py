medical_cause=input("Are you medically fit?Answer in Y or N:")
attend=int(input("Enter the attendance of the student:"))
if medical_cause=='Y':
    print("You are allowed")
else:
    if attend>=75:
        print ("Allowed")
    else:
        print ("You are not allowed")
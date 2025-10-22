print ("Select your ride!:")
print ("1. Bike")
print ("2. Car")
choice=int(input("Put the number of the ride you wish to select:"))
if (choice==1):
    print ("Which type of bike?:")
    print ("1.Scooter\n")
    print ("2.Scooty\n")
    choice2=int(input("Enter the number for the type of bike you wish:"))
    if (choice2==1):
        print("You have choosen the scooter")
    else:
        print("You have choosen the scooty")

elif (choice==2):
    print ("Which type of car?:")
    print ("1.Sedan")
    print ("2. SUV")
    choice3=int(input("Enter the number of the type of car you wish:"))
    if (choice3==1):
        print("You have choosen the Sedan")
    else:
        print("You have choosen the SUV")
else:
    print("Wrong Input!")
units =int(input("Enter the number of units that you have consumed or used up:"))
if (units<50):
    amount=units*2.60
    surcharge=25
elif(units<=100):
    amount=units*3.25
    surcharge=35
elif(units<=200):
    amount=130+162.50+((units-50)*3.25)
    surcharge=45
elif (units<=200):
    amount=130+162.50+((units-100)*5.26)
    surcharge=45
else :
    amount=130+162.50+526+((units-200*8.45))
    surcharge=75

total=amount+surcharge
print(total)
amount=int(input("Enter your desired amount:"))
note100=amount//100
note50=(amount%100)//50
note10=((amount%100)%50)//10
print("notes of 100 dollars",note100)
print("notes of 50 dollars",note50)
print("notes of 10 dollars",note10)
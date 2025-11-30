total=int(input("Enter the total bill amount:"))
paid=int(input("Enter the amount paid."))
due=total-paid
if paid<total:
    print("Due is to be paid of",due)
else:
    print("There is no total due to be paid.")
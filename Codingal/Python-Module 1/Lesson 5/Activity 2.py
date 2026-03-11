actual_cost=float(input("Please enter the actual cost of the item"))
sale_amount=float(input("Please enter the sale cost of the item"))
if (sale_amount>actual_cost):
    amount=sale_amount - actual_cost
    print("Total Profit={0}",format (amount))
else:
    print("No Profit!")
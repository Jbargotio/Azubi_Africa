charge = input("Please enter the charge of the food:")
Tip = 0.18 * int(charge)
Sales_Tax = 0.07 * int(charge)
Grand_Total = int(charge) + Tip + Sales_Tax
print("Tip = " + str(Tip))
print("Sales Tax = " + str(Sales_Tax))
print("Grand Total = " + str(Grand_Total))
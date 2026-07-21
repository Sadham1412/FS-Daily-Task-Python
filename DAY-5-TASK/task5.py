coffee = int(input("Enter the number of coffees: "))
coffee_price = 20
total_bill = coffee * coffee_price
print("\n------ Coffee Bill ------")
print("Coffee Ordered :", coffee)
print("Price per Coffee : Rs.", coffee_price)
print("Total Bill : Rs.", total_bill)
if total_bill > 100:
    discount = 30
    final_bill = total_bill - discount
    print("Discount : Rs.", discount)
    print("Final Bill : Rs.", final_bill)
else:
    print("No Discount Applied")
    print("Final Bill : Rs.", total_bill)

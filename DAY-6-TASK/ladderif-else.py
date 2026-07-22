#ladder if-else program example Electricity Bill
calculate_unit=int(input("enter the units"))
if calculate_unit>=200 and calculate_unit<=300:
    per_unit=2
    print("if you spend less than 100 unit per_unit price 2")
    print("your total bill is =",calculate_unit*per_unit)
elif calculate_unit>=301 and calculate_unit<=400:
    per_unit=3
    print("if you spend less than 101 between 200 unit per_unit price 3")
    print("your total bill is =",calculate_unit*per_unit)
elif calculate_unit>=401 and calculate_unit<=500:
    per_unit=5
    print("if you spend less than 201 between 300 unit per_unit price 5")
    print("your total bill is =",calculate_unit*per_unit)
elif calculate_unit>=501 and calculate_unit<600:
    per_unit=7
    print("if you spend less than 201 between 300 unit per_unit price 7")
    print("your total bill is =",calculate_unit*per_unit)
else:
    print("free")
    

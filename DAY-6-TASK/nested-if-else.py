#atm widthdraw example nested if else 
pin = int(input("enter your Pin: "))
if pin == 1234:
    balance = 5000
    amount = int(input("enter withdrawal amount: "))
    if amount <= balance:
        print("transaction successful")
        print("remaining balance:", balance - amount)
    else:
        print("insufficient balance")
else:
    print("incorrect pin")

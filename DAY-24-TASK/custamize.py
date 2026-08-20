class InsufficientBalanceError(Exception):
    pass
try:
    balance = 5000
    amount = int(input("Enter withdrawal amount: "))
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance =", balance)
except ValueError:
    print("Please enter numbers only")
except InsufficientBalanceError as e:
    print(e)

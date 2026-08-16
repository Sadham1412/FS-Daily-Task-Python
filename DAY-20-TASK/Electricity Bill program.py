# 1. Electricity Bill
# Calculate the electricity bill based on units:
# First 100 units: ₹2/unit
# Next 100 units: ₹3/unit
# Next 200 units: ₹5/unit
# Above 400 units: ₹7/unit
calculate=int(input("enter the unit"))
total_bill=0
if calculate<=100:
  total_bill=calculate*2
  print("=========electricity bill===========")
  print("total bill =",total_bill)
elif calculate>=100 and calculate<=200:
  total_bill=(100*2)+(calculate-100)*3
  print("=========electricity bill===========")
  print("total bill =",total_bill)
elif calculate >=200 and calculate <=400:
  total_bill=(100*2)+(100*3)+(calculate-100)*5
  print("=========electricity bill===========")
  print("total bill =",total_bill)
elif calculate>=400:
   total_bill=(100*2)+(100*3)+(100*5)+(calculate-100)*7
   print("=========electricity bill===========")
   print("total bill =",total_bill)

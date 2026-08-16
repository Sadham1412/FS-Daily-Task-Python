# 2. Salary Calculation
# Read basic salary and calculate gross salary based on:
# Basic ≤ 20,000 → HRA 20%, DA 50%
# Basic ≤ 40,000 → HRA 25%, DA 60%
# Above 40,000 → HRA 30%, DA 70%
salary=int(input("enter the salary"))
total_salary=0
if salary<=20000:
  HRA=(salary/100)*20
  DA=(HRA/100)*50
  salarygst=DA
  total_salary=salary-salarygst
  print("=========salary silp===========")
  print(total_salary)
elif salary<=40000:
  HRA=(salary/100)*25
  DA=(HRA/100)*60
  salarygst=DA
  total_salary=salary-salarygst
  print("=========salary silp===========")
  print(total_salary)
elif salary>40000:
  HRA=(salary/100)*30
  DA=(HRA/100)*70
  salarygst=DA
  total_salary=salary-salarygst
  print("=========salary silp===========")
  print(total_salary)

# no parameter no return
print(" example 1 no parameter no return")
def checkoddeven():
  value=3
  if value%2==0:
    print("Even number",value)
  else:
    print("Odd number",value)
checkoddeven()
# with parameter no return
print("example 2 with parameter no return ")
def checkoddeven(value):
  if value%2==0:
     print("Even number",value)
  else:
     print("Odd number",value)
checkoddeven(5)
# with parameter with return
print("example 3 with parameter with return ")
def checkoddeven(value):
  if value%2==0:
    return "Even"
  else:
    return "Odd"
print(checkoddeven(5))
# no parameter with return
print("example 4 no parameter with return ")
def checkoddeven():
  value=6
  if value%2==0:
    return "Even"
  else:
    return "Odd"
print(checkoddeven())

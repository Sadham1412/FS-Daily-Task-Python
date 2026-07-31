total=0
flag=True
while flag:
  score =int(input("enter the score"))
  if score!=0:
    total+=score
  else:
    break
print("total score:",total)

n=5 
for i in range(n):
  for j in range(n,i,-1):
    print(" ",end="")
  for k in range(i):
    if k==0 or k==i-1:
      print("*",end=" ")
    else:
      print("  ",end='')
  print()
for i in range(n,0,-1):
  for j in range(n,i,-1):
    print(" ",end="")
  for k in range(i):
    if k==0 or k==i-1:
      print("*",end=" ")
    else:
      print("  ",end='')
  print()

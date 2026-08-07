t=(1,2,3,4,2,1)
a=list(t)
b=[]
for i in range(len(a)):
  if a[i] not in b:
    b.append(a[i])
c=tuple(b)
print(c)

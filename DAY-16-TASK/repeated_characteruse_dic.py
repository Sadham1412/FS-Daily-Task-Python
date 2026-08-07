a="programming"
dic={}
for i in a:
  if i in dic:
    dic[i]+=1
  else:
    dic[i]=1
c=0
for i,j in dic.items():
  if j>1:
    c+=1
    print(i)
print("total repeated character=",c)

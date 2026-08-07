a="programming"
dic={}
for i in a:
  if i in dic:
    dic[i]+=1
  else:
    dic[i]=1
for i,j in dic.items():
  if j>1:
    print("first repeated character=",i)
    break

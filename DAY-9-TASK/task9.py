# using flag logic
'''
a=1
f=True
flag=True
while f==True:
    if flag:
        if a<=5:
            print(a,end="")
            a+=1
        else:
            flag=False
            a-=1
    else:
        if a>1:
            a-=1
            print(a,end="")
        else:
            f=False
'''
# using count method
c=1
a=1
while c<=9:
    print(a,end="")
    if c<5:
        a+=1
    else:
        a-=1
    c+=1
        
        

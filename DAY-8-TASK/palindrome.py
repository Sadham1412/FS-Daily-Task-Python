#conver to string method
a=int(input("enter the input:"))
a=str(a)
if a[::-1]==a:
    print("palinrome")
else:
    print("not a palinrome ")

# normal integer method
'''
check=123
temp=check
res=0
while temp>0:
    digit=temp%10
    res=res*10+digit
    temp=temp//10
if check == res:
     print("palinrome")
else:
     print("not a palinrome")
'''

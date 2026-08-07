
# move the zero last in list
a=[0,5,2,1,3,0,4]
b=[]
for i in a:
    if i==0:
        b.append(i)
        a.remove(i)
add_list=a+b
print(add_list)

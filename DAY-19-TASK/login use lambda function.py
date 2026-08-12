#ternary operator
u=lambda user,password : "loginsuccessful" if user=="sadham" and password=="1234" else "invaild"
print(u("sadham","1234"))
#normal check
x=lambda user,passw: user=="sadham" and passw=="1234"
if x("sadham","12"):
  print("login in sucess")
else:
  print("wrong")

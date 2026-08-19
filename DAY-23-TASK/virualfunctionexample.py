class teashop:
  def order(self): # this called virual function 
    self.id=1     
    self.name="sadham"
    print(self.id)
    print(self.name)
    print("your tea is ready within few mints")
class customer1(teashop):
  def order(self):
    self.id=2
    self.name="shanmuga"
    print(self.id)
    print(self.name)
    print("your tea ready")
c1=customer1()
c1.order()

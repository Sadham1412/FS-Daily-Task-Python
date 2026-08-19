class resume:
  def details(self):
    self.name=input("enter the name:")
    self.skill=input("enter you skill")
    self.education=input("enter you education")
    self.experience=input("enter the experiences")
    self.language=input("enter the language")
  def display(self):
    print("name:",self.name)
    print("skill:",self.skill)
    print("education:",self.education)
    print("experiences:",self.experience)
    print("language:",self.language)
r1=resume()
r1.details()
r1.display()
r2=resume()
r2.details()
r2.display()

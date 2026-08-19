# absract method example
from abc import ABC,abstractmethod
class payment(ABC):
  @abstractmethod
  def pay(self):
    pass
class upi(payment):
  def pay(self):
    print("paymeny done")
class creditcard(payment):
  def pay(self):
    print("creadited you amount")
u1=upi()
u1.pay()


class Product:
  def __init__(self,price):
    self._price = price

  @property
  def price(self):
    return self._price

  @price.setter
  def price(self,value):
    self._price = value

  @price.deleter
  def price(self):
    print("Deleting price")
    del self._price

p1 = Product(150)
print(p1.price)
p1.price = 200
print(p1.price)
del p1.price
class Plant:
  def __init__(self,name):
    self.name=name
  def __repr__(self):
    return "{}('{}')".format('Plant',self.name)

pl1 = Plant('Banyan')
pl2 = Plant('Neem')
pl3 = Plant('Ashoka')

print(pl1.__repr__())
print(pl1.__str__())
print(pl2.__repr__())
print(pl2.__str__())
print(pl3.__repr__())
print(pl3.__str__())


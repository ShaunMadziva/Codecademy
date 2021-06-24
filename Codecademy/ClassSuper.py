class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions

class SpecialPotatoSalad(PotatoSalad):
  def __init__(self, potatoes, celery, onions, raisins=None):
    super().__init__(potatoes, celery, onions)
    self.raisins = 40
  
#super() gives us a proxy object. With this proxy object, 
#we can invoke the method of an object’s parent class (also called its superclass). 
#We call the required function as a method on super()

sps = SpecialPotatoSalad(1,2,3)
print(sps.raisins)



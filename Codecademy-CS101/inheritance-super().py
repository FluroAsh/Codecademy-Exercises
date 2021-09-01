class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions

# Our 'special' class that modifies our parent class
# super() gives us a proxy object to invoke the method of our parent class
class SpecialPotatoSalad(PotatoSalad):
  def __init__(self, potatoes, celery, onions, raisins=None):
    super().__init__(potatoes, celery, onions)
    self.raisins = 40

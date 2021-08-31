class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  # __repr__() method to tell our class what we want the 'string representation' to be... Returns our .name attribute of the object automatically! 
  def __repr__(self):
    return 'Circle with radius {r}'.format(r=self.radius)
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(str(medium_pizza) + '\n' + str(teaching_table) + '\n' + str(round_room))

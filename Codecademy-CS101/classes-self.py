class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Takes our passed diameter and calculates the radius
    self.radius = diameter / 2

  # Method to calculate circumference   
  def circumference (self):
    return 2 * self.pi * self.radius

# Initialized our values
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

# Must include our circumference object, otherwise will not print correctly, follows the format .circumference() so we can RETURN our value to the string
print('\n' + str(medium_pizza.circumference()) + '\n' + str(teaching_table.circumference()) + '\n' + str(round_room.circumference()))

class Circle:
  pi = 3.14
  def area(self, radius):
    return Circle.pi * radius ** 2

# Instantiate our class so it can be used... 
circle = Circle()

# Get the area from our class function 'area'
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)

print(str(pizza_area) + '\n' + str(teaching_table_area) + '\n' + str(round_room_area))

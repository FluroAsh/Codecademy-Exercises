class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print('New circle with diameter: {diameter}'.format(diameter=diameter))

# Don't need to specify our function as it is self-intialized when we call the class (note the lack of intiliazation)
teaching_table = Circle(36)

class HashMap:
  
  def __init__(self, array_size):
    self.array_size = array_size 
    ''' List comprehension to create a list as length specified in array_size
    Each element set to None'''
    self.array = [None for i in range(self.array_size)]

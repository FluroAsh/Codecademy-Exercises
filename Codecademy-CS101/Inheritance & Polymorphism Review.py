class SortedList(list):
  # Super used to invoke parent class (list)
  def append(self, value):
    # Performs .append, borrowed from our parent class (list)!
    super().append(value) 
    self.sort() # Self is the list in question here!

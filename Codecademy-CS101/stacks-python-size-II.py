from node import Node

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      # Increment stack size by 1 here:
      self.size += 1

  def pop(self):
    if not self.is_empty:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This stack is totally empty.")
  
  def peek(self):
    if not self.is_empty:
      return self.top_item.get_value()
    else:
      print("Nothing to see here!")
      
  # If our limit is greater than size, we have space!
  def has_space(self):
    return self.limit > self.size

  # Helper method to see if our stack is empty!  
  def is_empty(self):
    return self.size == 0

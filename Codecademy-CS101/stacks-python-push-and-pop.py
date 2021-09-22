from node import Node

class Stack:
  def __init__(self):
    self.top_item = None
  
  # Define your push() and pop() methods below:
  ''' 
  Push method 'pushes' our top item to the bottom, as we are now
  placing 'item' on top. Reflected in 'self.top_item = item'
  '''
  def push(self, value):
    item = Node(value)
    item.set_next_node(self.top_item) 
    self.top_item = item
    
  def pop(self): # 'Pop' off our top item and return its value!
      item_to_remove = self.top_item
      # Must remember to set our new top_item to the node that
      # follows the one we have removed!
      self.top_item.set_next_node(item_to_remove) 
      return item_to_remove.get_value()
  
  def peek(self):
    return self.top_item.get_value()

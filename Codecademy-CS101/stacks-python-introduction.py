from node import Node

class Stack:
  def __init__(self):
    self.top_item = None

  # Take a peek out our top value... ;)
  # Uses our imported Node class!
  def peek(self):
    return self.top_item.get_value() 

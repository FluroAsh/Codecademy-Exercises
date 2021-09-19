from node import Node

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
  
  # Return the value of our stack's head using theNode method get_value()
  def peek(self):
    return Node.get_value(self.head) 

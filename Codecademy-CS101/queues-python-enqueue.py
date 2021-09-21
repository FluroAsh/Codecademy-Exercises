from node import Node

class Queue:
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0
    
  # ENQUEUE METHOD 
  def enqueue(self, value):
    if self.has_space():
      item_to_add = Node(value) # Instantiates the node with our value
      print("Adding " + str(item_to_add.get_value()) + " to the queue!")
      
      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
      self.size += 1 # Because we have space, increase size by 1
    else: 
      print("Sorry, no more room!")
      
  def peek(self):
    if self.is_empty():
      print("Nothing to see here!")
    else:
      return self.head.get_value()
  
  def get_size(self):
    return self.size
  
  def has_space(self):
    if self.max_size == None:
      return True
    else:
      return self.max_size > self.get_size()
    
  def is_empty(self):
    return self.size == 0

q = Queue()
q.enqueue("all the fluffy kitties")

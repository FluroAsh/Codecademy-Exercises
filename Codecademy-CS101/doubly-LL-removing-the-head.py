class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value
    

class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None

  # ADD -> HEAD METHOD
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node

    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)

    self.head_node = new_head # Update class head_node!

    if self.tail_node == None:
      self.tail_node = new_head

  # ADD -> TAIL METHOD
  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node

    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)

    self.tail_node = new_tail # Update class tail_node!

    if self.head_node == None:
      self.head_node = new_tail
  
  # REMOVE HEAD METHOD
  def remove_head(self):
    # We're removing our head_node in this method
    removed_head = self.head_node

    if removed_head == None:
      return None # Nothing to remove!
    
    self.head_node = removed_head.get_next_node() # Get our new head, as we have removed the old head - update class var

    if self.head_node != None: # Set previous node to None, as the head shouldn't have a prev node
      self.head_node.set_prev_node(None)
    
    if removed_head == self.tail_node:
      self.remove_tail() # Need to remove tail as head/tail are the same in this scenario
    return removed_head.get_value()

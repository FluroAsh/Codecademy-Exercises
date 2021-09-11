# Our Node Class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
# insert_beginning and stringify_list methods:
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node  
  
  def stringify_list(self):
    string_list = ''
    current_node = self.get_head_node()
    while current_node: # While current_node = True 
      '''If the value in current_node is NOT equal to None.
      Add string from current_node 'value' to our list and 
      get the next node'''
      if current_node.get_value() != None: 
        string_list += str(current_node.get_value()) + '\n'
      current_node = current_node.get_next_node()
    return string_list
 
 
# Test Code
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())

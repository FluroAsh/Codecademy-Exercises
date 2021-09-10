class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def set_link_node(self, link_node):
    self.link_node = link_node
    
  def get_link_node(self):
    return self.link_node
  
  def get_value(self):
    return self.value

# Create Nodes
yacko = Node('likes to yak')
wacko = Node('has a penchant for hoarding snacks')
dot = Node('enjoys spending time in movie lots')

# Link the Nodes: y -> d... d -> w
Node.set_link_node(yacko, dot)
Node.set_link_node(dot, wacko)

# Get our link with the stored data... 
# eg. get value stored in 'yacko' from 'dots' link node ('enjoys spending time in movies lots')
dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()
print(dots_data)
print(wackos_data)

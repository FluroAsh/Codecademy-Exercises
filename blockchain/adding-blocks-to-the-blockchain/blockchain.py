#imports the Block class from block.py
from block import Block
class Blockchain:
 
  def __init__(self):
    self.chain = []
    self.all_transactions = []
    self.genesis_block()
 
   def genesis_block(self):
    transactions = {}
    genesis_block = Block(transactions, "0")
    self.chain.append(genesis_block)
    return self.chain
 
 # prints contents of blockchain
  def print_blocks(self):
    for i in range(len(self.chain)):
      current_block = self.chain[i]
      print("Block {} {}".format(i, current_block))
      current_block.print_contents()    
  
  # add block to blockchain `chain`
  def add_block(self, transactions):
    # self.chain[len(self.chain))-1] gets the previous blocks dictionary
    # .hash then retrieves the actual value associated with hash key
    new_block = Block(transactions,self.chain[len(self.chain)-1].hash)
    self.chain.append(new_block)
    return 

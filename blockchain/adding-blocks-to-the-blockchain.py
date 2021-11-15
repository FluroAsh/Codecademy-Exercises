Now that we have everything in place, let’s begin adding blocks to the blockchain.
---
[Hint: The proper way to access a specific block’s hash from the chain is through this line of code: self.chain[index].hash. 
- The previous block can be accessed by self.chain[len(self.chain)-1].
- Your resulting code should be as follows: Block(transactions, previous_block_hash)]

-
1. Complete the function add_block().

To do this, create a variable named new_block that takes in a transaction and the previous_block‘s hash. Append new_block to the end of the chain.

```
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
    # self.chain[len(self.chain))-1] gets the previous_hash dictionary
    # .hash then retrieves the actual value associated with the key
    new_block = Block(transactions,self.chain[len(self.chain)-1].hash)
    self.chain.append(new_block)
    return 
```

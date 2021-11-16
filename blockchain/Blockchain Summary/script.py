from blockchain import Blockchain

block_one_transactions = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
block_two_transactions = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Cole", "amount":"35"}
fake_transactions = {"sender": "Bob", "receiver":"Cole, Alice", "amount":"25"}

# Initalize the blockchain & print contents
local_blockchain = Blockchain()
local_blockchain.print_blocks()
print('\n')

local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
# Targets 2nd block and replaces transactions with fake_transactions (generates a different hash)
local_blockchain.chain[2].transactions = fake_transactions
local_blockchain.validate_chain()
# Block 2 is invalid as block 3's previous hash does not match block 2's current hash

local_blockchain.print_blocks()

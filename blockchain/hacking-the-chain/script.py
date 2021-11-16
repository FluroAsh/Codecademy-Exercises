from blockchain import Blockchain

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

my_blockchain = Blockchain()
my_blockchain.add_block(new_transactions)
my_blockchain.print_blocks()

# Get the transactions from our first block and replace with
# "fake_transactions"
my_blockchain.chain[1].transactions = "fake_transactions"

# Validate the blockchain's integrity by checking the generated hash's
# against what is currently stored in each block
my_blockchain.validate_chain()

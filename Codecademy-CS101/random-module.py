# Import random below:
import random

# Random List - Method at the beginning, then for i which is a placeholder and 
# finally our range which will populate 100 different variables in our list
random_list = [random.randint(1,100) for num in range(101)]

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

# Combine our two lists: drinks, caffeine
zipped_drinks = zip(drinks, caffeine)

# Convert the zipped_drinks list into key:value format. For every key get the value in zip(drinks, caffeine)
drinks_to_caffeine = {key:value for key, value in zip(drinks, caffeine)}
print(drinks_to_caffeine)

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

# Search value contained in key 'stamina grains' and add it to health points. Nothing is found? Return default value '0'. Repeat for 'power stew' and 'mystic bread'
health_points += available_items.pop('stamina grains', 0)
health_points += available_items.pop('power stew', 0)
health_points += available_items.pop('mystic bread', 0)

print('Available Items: ' + str(available_items) + '\n\n' + 'Health Points: ' + str(health_points))

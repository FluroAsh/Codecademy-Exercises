caffeine_level = {'espresso': 64, 'chai': 40, 'decaf': 0, 'drip': 120}

caffeine_level['matcha'] = 30

# Try to print caffeine_level['matcha'] if it exists, if not throw our KeyError...
try:
  print(caffeine_level['matcha'])
except KeyError:
  print('Unknown Caffeine Level')

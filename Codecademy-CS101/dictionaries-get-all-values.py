num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

# For every 'value'/exercise in num_exercises, add this to 'total_exercises' (our global variable as above)
for exercise in num_exercises.values():
  total_exercises += exercise
print(total_exercises)

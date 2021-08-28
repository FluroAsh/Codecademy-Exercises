grades = [90, 88, 62, 76, 74, 89, 48, 57]
# (Option 1 - Elegant) scaled_grades = [score + 10 for score in grades]

# (Option 2)
scaled_grades = []

for score in grades:
  scaled_grades.append(score + 10)

print(scaled_grades)

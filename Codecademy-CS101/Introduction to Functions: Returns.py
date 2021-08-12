current_budget = 3500.75

# Function to determine the current budget as declared in current_budget
def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

# Function to determine the budget minus expenses for our budget
def deduct_expense(budget, expense):
  return budget - expense

shirt_expense = 9

# Call the deduct_expense function and pass our current budget and shirt expense to generate the new budget minus expenses
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)



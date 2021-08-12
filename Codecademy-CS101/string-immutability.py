first_name = "Bob"
last_name = "Daily"

# Strings are immutable... Therefore, we must create a new name with R + the 
# last 2 letters of B(ob) to fix the typo!
fixed_first_name = 'R' + first_name[-2:]
print(first_name)

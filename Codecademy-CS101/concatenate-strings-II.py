first_name = "Reiko"
last_name = "Matsuki"

# Using a len() statement as the starting index and omitting the final index lets you slice 'n' characters 
# from the end of a string, where 'n' is the amount you subtract from len().
def password_generator(first_name, last_name):
  return first_name[len(first_name)-3:] + last_name[len(last_name)-3:]

temp_password = password_generator(first_name, last_name)
print(temp_password)

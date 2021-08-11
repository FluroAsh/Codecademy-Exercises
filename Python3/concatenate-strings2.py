first_name = "Reiko"
last_name = "Matsuki"

# Rembber the colon, important as this indicates we want the last 3 
# elements, not just the value located at index -3 (not including the # colon would return 'iu')
def password_generator(first_name, last_name):
  return (first_name[-3:] + last_name[-3:])

temp_password = password_generator(first_name, last_name)

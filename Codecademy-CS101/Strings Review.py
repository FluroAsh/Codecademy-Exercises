first_name = 'Abe'
last_name = 'Simpson'

def username_generator(first_name, last_name):
  return first_name[:3] + last_name[:4]

# Password begins by being temp blank, then loops through each index in our string using len to find the end index. 
# It then assigns the index -1 so that it shifts to the left one place and returns our password. 
def password_generator(user_name):
  password = ''
  for i in range(0, len(user_name)):
    password += user_name[i-1]
  return password

user_name = username_generator(first_name, last_name)
password = password_generator(user_name)

print(user_name)
print(password)

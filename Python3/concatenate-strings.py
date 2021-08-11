'''Copeland’s Corporate Company has realized that their policy of using the first five letters of an employee’s last name as a user name isn’t ideal when they have multiple employees with the same last name.

Write a function called account_generator() that takes two inputs, first_name and last_name and concatenates the first three letters of each and then returns the new account name.'''

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  return (first_name[0:3] + last_name[0:3])
  
new_account = account_generator(first_name, last_name)
print(new_account)

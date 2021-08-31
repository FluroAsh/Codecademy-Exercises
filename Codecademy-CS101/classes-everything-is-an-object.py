dir(5)

def this_function_is_an_object(word):
  return word.upper()

# Test the function
print(this_function_is_an_object('hey!'))
print('\n')

# Get the ATTRIBUTES of our object 
print(dir(this_function_is_an_object))

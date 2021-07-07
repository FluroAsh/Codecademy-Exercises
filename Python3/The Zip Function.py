owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

# Convert into 1 list - prints reference from memory
names_and_dogs_names = zip(owners, dogs_names)
print(names_and_dogs_names, "\n")

# We can also just print it directly like this:
'print(list(names_and_dogs_names))'

# Convert into readable list, assign to a tuple 
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

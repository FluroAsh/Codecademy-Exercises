can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

# For every element in our list, check to see if it contains the 'count' attribute, then print 
for element in can_we_count_it:
  if hasattr(element, 'count'):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")

"""Let’s go over the terminal output of the past two instructions. You should see the following output in your terminal right now:

<class 'dict'> does not have the count attribute :(
<class 'str'> has the count attribute!
<class 'int'> does not have the count attribute :(
<class 'list'> has the count attribute!

This is because dictionaries and integers both do not have a count attribute, while strings and lists do. In this exercise, we have iterated through can_we_count_it and
used hasattr() to determine which elements have a count attribute. """

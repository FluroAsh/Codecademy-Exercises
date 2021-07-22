# Types of Arguments -- Default, Positional & Keyword Arguments 
def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + " and lastly " + final_destination)

# Postional Arguments
trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
trip_planner("Iceland", "Germany", "India")
# Keyword Arguments
trip_planner(first_destination = "Iceland", second_destination = "India", final_destination = "Germany")
# Positional Arguments - 2 Arguments Only
trip_planner("Brooklyn", "Queens")

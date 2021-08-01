# Function to welcome the user to our program
def trip_planner_welcome(name):
  print("Welcome to TripPlanner v1.0 " + name)

# Function for destination information, mode_of_transport DEFAULT VALUE of "Car"
def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  # This print is converted to a string as estimated_time is a decmial
  print("It will take approximately " + str(estimated_time) + " hours")
  
def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

# Call the above functions with given values 
## Changing "Car" to another value will change our default value! 
trip_planner_welcome("Ashley")
estimate = estimated_time_rounded(16.45)
destination_setup("Melbourne ", "Tokyo ", estimate, "Plane")

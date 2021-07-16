#  4 Arguments to calculate the total of a holiday trip
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  #print("Your total is: $" + str(car_rental_total + hotel_total + plane_ticket_price))
  print("Your total is: ${0}".format(car_rental_total + hotel_total + plane_ticket_price))

# Pass the values to the function
calculate_expenses(200, 100, 100, 5)

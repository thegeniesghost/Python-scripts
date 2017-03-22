# The 'cars' variable is how many cars there are.
cars = 100

# the 'space_in_car' variable is how much space is in each car. 
space_in_car = 4.0

# The 'drivers' variable is how many driver there are.
drivers = 30

# The 'passengers' variable is how many passengers there is.
passengers = 90

# The 'cars_not_driven' is a variable for the cars not in use at the moment (atm).
cars_not_driven = cars - drivers

# The 'cars_driven' is a variable for how many cars that are in use at the moment (atm).
cars_driven = drivers

# The 'carpool_capacity' is a variable with how many people are currently in all the cars.
carpool_capacity = cars_driven * space_in_car

# The 'average_passengers_per_car' is a variable with the average passengers per car.
average_passengers_per_car = passengers /cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We need to put about", average_passengers_per_car, "in each car."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
cars  = 100
# This line defines the value of the cars variable.

space_in_a_car = 4
# This line defines the value of the "seats in each car" variable.

drivers = 30
# This line defines the value of the drivers variable.

passengers = 90
# This line defines the value of the passengers variable.

cars_not_driven = cars - drivers
# This line defines the "cars not driven" value by subtracting the pre-defined drivers variable from the cars variable.

cars_driven = drivers
# This line defines the "cars drive" variable as equal to the drivers variable.

carpool_capacity = cars_driven * space_in_a_car
# This line defines the capacity variable by multiplying the pre-defined "cars driven" and "seats in each car" variables.

average_passengers_per_car = passengers / cars_driven
# This line defines the "average people per car" variable by dividing the passenger variable by the "cars driven" variable.

print "There are", cars, "cars available."
# This line displays some text, referencing the cars variable.

print "There are only", drivers, "drivers available."
# This line displays some text, referencing the drivers variable.

print "There will be", cars_not_driven, "empty cars today."
# This line displays some text, referencing the "cars not driven" variable.

print "We can transport", carpool_capacity, "people today."
# This line displays some text, referencing the capacity variable.

print "We have", passengers, "to carpool today."
# This line displays some text, referencing the passengers variable.

print "we need to put about", average_passengers_per_car, "in each car."
# This line displays some text, referencing the "average passengers" variable.

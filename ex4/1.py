cars=100
space_in_cars=4.0				#these are variables
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_cars
average_passengers_per_car=passengers/cars_driven

print"there are",cars,"cars available"
print"there are only",drivers,"drivers available"
print"there will be",cars_not_driven,"empty car today"
print"we can traport",carpool_capacity,"people today"
print"we have",passengers,"to carpool today"
print"we need to put about",average_passengers_per_car,"in each car"

#remember declare varible in starting name must match in print statement

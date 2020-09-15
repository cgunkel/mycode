#!/usr/bin/env python3

#Create a list called cars
cars = [{'type': 'convertible', 'year': '1991', 'color': 'red'}, {'type': 'suv', 'year': '2001', 'color': 'black'}, {'type': 'truck', 'year': '2020', 'color': 'grey'}]
#Each dictionary needs to have the keys type, year, color (you fill out values)

# For each of the three car dictionaries, print out the sentece
# "I want a <color> <type> from <year>."
# This works but is time consuming
#Test1
car1 = f"I want a {cars[0]['color']} {cars[0]['type']} from {cars[0]['year']}"
car2 = f"I want a {cars[1]['color']} {cars[1]['type']} from {cars[1]['year']}"
car3 = f"I want a {cars[2]['color']} {cars[2]['type']} from {cars[2]['year']}"
print(car1)
print(car2)
print(car3)

#Test 2 using for loop
for car in cars:
	print(f"I want a {car['color']} {car['type']} from {car['year']}.")


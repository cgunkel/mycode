#!/usr/bin/env python3

# Create a list of animals called animal_list1

animal_list1 = ["Fox", "Fly", "Ant", "Bee", "Cod", "Cat", "Dog", "Yak", "Cow", "Hen", "Koi", "Hog", "Jay", "Kit"]
print(animal_list1)

print(animal_list1.index("Ant"))
print(animal_list1[7])

# List number and value for list until end of file
#for tup in enumerate(animal_list1):
#    print(tup)

# The pop command will remove and item from your list.
## animal_list1.pop()
##  print(animal_list1)

fish = animal_list1[9:]
print(fish)

# Print a range of animals
r_animals = animal_list1[3:7]
print(r_animals)

# Instead of printing them one at a time and referencing ach item use a for loop
for x in animal_list1:
    print(x)


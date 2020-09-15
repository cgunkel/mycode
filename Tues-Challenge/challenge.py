#!/usr/bin/env python3

# Pets list
pets = ['fido', 'spot', 'fluffy']

print(pets)

# Add first animal
animal_1 = input ("Name an animal: ")

# Add second animal
animal_2 = input ("Name another animal: ")

# Add third animal
animal_3 = input ("one last time: ")
print(animal_1)
print(animal_2)
print(animal_3)

# Method 1
pets.append(animal_1)
pets.append(animal_2)
pets.append(animal_3)
print(pets)
print(enumerate(pets))
for ind, val in enumerate(pets):
    print(ind, val)



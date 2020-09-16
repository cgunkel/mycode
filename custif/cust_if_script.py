#!/usr/bin/env python3
  
message = "The Saffir-Simpson scale for hurricane and tropical storms indicates you are in a "

# wrap connection in a float() to accept decimals as numbers
connection = float(input("What is the wind speed where you are at? "))

# if input value was higher or equal to 157
if connection >= 157:
    message = message + "Category 5 hurricane."
elif connection >= 130:
    message = message + "Category 4 hurricane."
elif connection >= 111:
    message = message + "Category 3 hurricane."
elif connection >= 96:
    message = message + "Category 2 hurricane."
elif connection >= 74:
    message = message + "Category 1 hurricane."
else:
    message = "C'mon you think this is a storm?"
print(message)

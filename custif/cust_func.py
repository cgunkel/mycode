#!/usr/bin/env python3

import csv

with open("Data_4CustFunc.csv", "r") as configfile:
    windspeed = configfile.readlines()

print(windspeed)


#message = "The Saffir-Simpson scale for hurricane and tropical storms indicates you are in a "

# wrap connection in a float() to accept decimals as numbers
windspeed = float(input("What is the wind speed where you are at? "))

# if input value was higher or equal to 157
if windspeed >= 157:
    message = message + "Category 5 hurricane."
elif windspeed >= 130:
    message = message + "Category 4 hurricane."
elif windspeed >= 111:
    message = message + "Category 3 hurricane."
elif windspeed >= 96:
    message = message + "Category 2 hurricane."
elif windspeed >= 74:
    message = message + "Category 1 hurricane."
else:
    message = "C'mon you think this is a storm?"
print(message)

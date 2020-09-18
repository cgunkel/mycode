#!/usr/bin/env python3

import csv

# Read in data
def windspeed_reader():
    with open("Data_4CustFunc.csv", "r") as f:
        lines = csv.reader(f)
        speeds = []
        for line in lines:
            speeds.append(line)
    return speeds
    
# windspeed = float(input("What is the wind speed where you are at? "))

#  check the windspeed agains the cattegories of hurricanes
def hurricane_category(windspeed):
    message = "The Saffir-Simpson scale for hurricane and tropical storms indicates you are in a "
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
    return message

def main():
    for location in windspeed_reader:
        state = location[0]
        windspeed = int(location[1])
        message= hurricane_category(windspeed)
        #print(f"For winds of {windspeed}'s {message}")
        print(state, windspeed, message)    
main()

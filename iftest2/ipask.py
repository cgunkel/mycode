#!/usr/bin/env python3

ipchk = input("Apply an IP address: ") # Prompts user for an ip address

# a provided string will test true
if ipchk:
    print("Looks like the IP address was set: " + ipchk) # indented under if statement
else:    # If data is not provided
    print("You did not provide input.")    # indented under else


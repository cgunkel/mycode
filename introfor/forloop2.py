#!/usr/bin/env python3
# create a list of strings
vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
# create a second list of strings

approved_vendors = ["cisco", "juniper", "big_ip"]

# Loop across the list called vendors
for x in vendors:
    print("\nThe vendor is " + x, end="")  #newlinte, print current vendor and end without a new line
    if x not in approved_vendors:  # if x does not apper with the list approved_vendors
        print(" - NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended.") # print when loop has finished

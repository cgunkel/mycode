#!/usr/bin/env python3

ipchk = input("Apply an IP address: ")    # this line now prompts for input

# if user set IP of gateway
if ipchk == "192.168.70.1":
    print("Looks like the IP address for the Gateway was set: " + ipchk + " This is not recommended.")
elif ipchk:
    print("Looks like the IP address was set: " + ipchk)    #indented under if
else:    #if data is not entered
    print("You did not provide input.")    # indented under else

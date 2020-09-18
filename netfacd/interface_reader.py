#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())
for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    try:    # This ia a new line, you also nee to indent the code below this line
        #print(netifaces.ifaddresses(i)[netifaces.AF_LINK])
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) # Print the MAC
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) # Print the IP
    except:    # This is a new line
        print("Could not colect adapter information") # Print an error message

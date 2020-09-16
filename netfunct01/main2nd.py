#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

# funtion to push commands
def commandpush(devicecmd): # devicecmd==list
    for coffeetime in devicecmd.keys():
        print('Handshaking. .. ... connecting with ' + coffeetime)
        # we'll learn to write code that connect to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + mycmds)
            # we'll learn to write code that sends cmds to device here

# function to reboot devices
def devicereboot(devicecmd): #devicecmd==list
    for coffeetime in devicecmd.keys():
        print('Connecting to.. ' + coffeetime)
        # we will learn to write code to connect to devices here
        print('REBOOTING NOW!')
        # we will learn to wrote code to send cmds to reboot device


# start our main script
def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}
    # data that replaces data stored in file

    print("Welcome to the network device command pusher") # Welcome message

    ## get data seet
    print("\nData set found\n") # replace with function call that reads in the data from file

    ## run
    commandpush(work2do)  # call function to push commands to devices
    print("\nWe will now reboot the devices\n")
    devicereboot(work2do) # call function to reboot devices
# call our main function
main()

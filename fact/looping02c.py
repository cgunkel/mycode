#!/usr/bin/env python3

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile object open
    # loop over lines
    for svr in dnsfile:
        # print and end without a new line
        print(svr, end="")
# no need to close our file - closed automatically

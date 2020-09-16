#!/usr/bin/python3
# parse keystone.common.wsgi and return number of failed login attempts

loginsuccess = 0 # counter for fails

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:


    # loop over the list of lines
    for line in kfile:
    # if this 'fail pattern' appear in the line...
        if "- - - - -] Loaded 2 encryption keys" in line:
            loginsuccess +=1 # this is the same as loginfail = loginfail + 1

print("The number of valid log in attempts is ", loginsuccess)


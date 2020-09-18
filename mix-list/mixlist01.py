#!/usr/bin/env python3

# Create a list call my_list
my_list = [ "192.168.0.5", 5060, "UP" ]

# Print the ip address
print("The first item in the list (IP): " + my_list[0] )

# Now we are printing the port which is a string
print("The second item in the list (port): " + str(my_list[1]) )

# We are now printing the status
print("The last item in the list (state): " + my_list[2] )

# Create a second list call new_list
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# When I ssh into IP addresses 10.0.0.1 or 10.20.30.1 I am unable to ping ports 5060, 80, or 55.
print ("When I", new_list[5], "into the ip address", new_list[3], "or", new_list[4], "I am unable to ping ports", str(new_list[0]), ",", new_list[1], ", or", str(new_list[2]))

# Concatenate Method for printing a line
print(new_list)
print(type(new_list[0]))
print(type(new_list[1]))
print(type(new_list[2]))
print(type(new_list[3]))
print(type(new_list[4]))
print(type(new_list[5]))
sentence_01 = "When I " + new_list[5] + " into IP addresses " + new_list[3] + " or, " + new_list[4] + " I am unable to ping ports " + str(new_list[0]) + ", " + new_list[1] + ", or " + str(new_list[2])
print(sentence_01)

# .format() Method for printing a line
sentence_03 = "When I {5} into IP addresses {3} or, {4} I am unable to ping ports {0}, {1}, or {2}." .format(*new_list)
print(sentence_03)

#f-string
sentence_02 = f"When I {new_list[5]} into IP addresses {new_list[3]} or, {new_list[4]} I am unable to ping ports {new_list[0]}, {new_list[1]}, or {new_list[2]}."
print(sentence_02)

#!/usr/bin/env python3

# Creat a list called list1
list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

# Display list1 
print(list1)

# Display list1[1] which should only display arista_eos
print(list1[1])

# Create a new list containing a single item
list2 = ["juniper"]

# Extend list1 by list2 (combining both lists togetrher into a single list
list1.extend(list2)

# Display list1, which now contains juniper
print(list1)

# Create list3
list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

#Us the append operation to append list1 by list3
list1.append(list3)

# Display the name complext list1
print(list1)

# Display list item 5
print(list1[4])

# Display the first ip address
print(list1[4][1])

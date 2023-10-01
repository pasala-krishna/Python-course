# Write a Python program to find the common elements between two lists.

list1 = ['a','b','c']
list2 = ['c','d','e']

# convert lists to sets

set1 = set(list1)
set2 = set(list2)

# printing common set elements by inserction operartor

print(set1&set2)
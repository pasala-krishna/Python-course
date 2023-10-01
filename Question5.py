# Write a Python program to reverse a list in place (without creating a new list).

list1 = [5,4,3,2,1]
# storing beginning and ending indices 
left = 0
right = len(list1) - 1

# reversing the list by comparing indicies 
while(left < right):
    temp = list1[right]
    list1[right] = list1[left]
    list1[left] = temp
    
    left = left + 1
    right = right - 1
    
print(repr(list1))
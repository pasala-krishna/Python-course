# Write a program that finds the largest element in a list of. The input must be from user

#take the number of list elements form the user
num = int(input('Enter the no.of elements: '))
list1 = []
# taking inputs from user and appending into the list
for i in range(num):
    x = float(input('enter the number: '))
    list1.append(x)
# sorting the list
list1.sort()
print('the largest element in the list is ', list1[-1])
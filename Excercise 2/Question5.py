# Write a function square_even_numbers that takes a list of integers, squares the even numbers, and returns a new list.

def square_even_numbers(numbers):
    
    i = 0
    while i< len(numbers):
        if numbers[i] % 2 == 0:
            numbers[i] = numbers[i] **2
            i += 1
        else:
            i += 1
            continue
    
list1 = [1, 2, 3, 4, 5] # test case 1
square_even_numbers(list1)

print('result of first test case is: ', list1)

list2 = [10, 15, 20, 25] # test case 2
square_even_numbers(list2)

print('result of second test case is: ', list2)
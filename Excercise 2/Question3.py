#  Write a function multiply_elements that takes a list of numbers and returns their product using a lambda function.

# one way to solve
def multiply_elements(numbers):
    # Use a lambda function to multiply elements in the list
    product = lambda x, y: x * y

    # Initialize the result with the first element of the list
    result = numbers[0]

    # Multiply each element in the list with the result
    for num in numbers[1:]:
        result = product(result, num)

    return result


# Test Cases:

"""
first medhod testing

numbers_list1 = [2, 3, 4]
result1 = multiply_elements(numbers_list1)
print("Test case 1:", result1)

numbers_list2 = [5, 6, 7]
result2 = multiply_elements(numbers_list2)
print("Test case 2:", result2)

"""

#second menthod to solve

from functools import reduce

def multiply_elements2(numbers):

    result = reduce((lambda x,y: x*y), numbers)
    return result

# testing test cases

list1 = [2, 3, 4]
list2 = [5, 6, 7]

result1 = multiply_elements2(list1)
print("Test case 1:", result1)
result2 = multiply_elements2(list2)
print("Test case 2:", result2)
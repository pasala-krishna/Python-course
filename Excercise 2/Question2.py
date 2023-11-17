# Write a function calculate_factorial that calculates the factorial of a non-negative integer using recursion.Write a function calculate_factorial that calculates the factorial of a non-negative integer using recursion.

# taking input from the user
input_flag = True
while input_flag == True:
    user_input = int(input('Enter a positive number: '))
    
    if user_input > 0:
        input_flag = False
    else:
        print('Error: invalid input')

# function to calculate factorial

def calculate_factorial(num):
    if num ==0:
        return 1
    factorial = 1
    for i in range(1, num +1):
        factorial *= i
        
    return factorial

result = calculate_factorial(user_input)
print(result)
# Write a function calculate_power that takes two integers as input and returns the base raised to the exponent.

# Taking input from the user
input_base = int(input('Enter the base value: '))
input_exponent = int(input('Enter the exponent value: '))

# calculating the value using function
def calculate_power(base,exponent):
    return base** exponent

result = calculate_power(input_base,input_exponent)
print(f'The base {input_base} raised to the {input_exponent} is {result}')
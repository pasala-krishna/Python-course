# Write a Python function calculate_tax that calculates the income tax based on a given income. Use a lambda function for the tax calculation. The tax is 30%

calulate_tax = lambda x: x * (30/100)

income1 = 50000
print(f'income tax for the income {income1} is: {calulate_tax(income1)}')

income2 = 100000
print(f'income tax for the income {income2} is: {calulate_tax(income2)}')
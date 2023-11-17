class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2

# Example usage:
calculator = Calculator()

result_addition = calculator.add(5, 3)
print(f"5 + 3 = {result_addition}")

result_subtraction = calculator.subtract(10, 4)
print(f"10 - 4 = {result_subtraction}")

result_multiplication = calculator.multiply(6, 2)
print(f"6 * 2 = {result_multiplication}")

result_division = calculator.divide(8, 2)
print(f"8 / 2 = {result_division}")

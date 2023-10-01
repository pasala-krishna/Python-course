# Write a Python program to calculate the factorial of a given number.

# take an input from the user
num = int(input('enter a number: '))
fact = 1
# if the number is zero the factorial is always 1
if num == 0:
    print(fact)
# finding factorial for numbers other than zero
for i in range(1,num+1):
    fact = fact*i

print(fact)
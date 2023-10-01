# Write a Python program that finds all prime numbers within a specified range
# taking iput of lower range and upper range from the user
lower = int(input('enter a lower range number: '))
upper = int(input('enter a upper range number: '))

print(f'prime numbers between {lower} and {upper} are')

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
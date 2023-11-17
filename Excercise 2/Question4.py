# Write a Python function power that takes two integers, base and exponent, as arguments and returns the result of base^exponent using recursion.

def power(base,exponent):
   if exponent == 0:
       return 1 
   
   result = base * power(base, exponent -1)
   return result

result1 = power(2,3) # Test case 1
print(f'power of  2 and 3 is {result1}')

result2 = power(5,2) # Test case 2
print(f'power of  5 and 2 is {result2}')

    
    
# Write a function increment_by that takes a number and returns a function that increments its input by a specified amount.

def increment_by(increment_amount):
    def increment(num):
        return increment_amount +num
    
    return increment # this creates a closure

# test case
increment_by_5 = increment_by(5)
print(increment_by_5)

# calling the returened functionn with 3

print('incrementing 3 by 5 using function is: ', increment_by_5(3))



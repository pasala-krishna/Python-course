# Write a Python program that checks if a given string is a palindrome or not (ignoring spaces and capitalization).

# taking input from the user
str1 = input(' enter a string: ')

# lowering the sting case and replacing the white spaces
str1 = str1.lower().replace(' ', '')

#reversing the string
st2 = str1[::-1]
# evaluating for palaindrome
if(str1 == st2):
    print('the string is a palindrome')
else:
    print('the string is not a palindrome')
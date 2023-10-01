# Write a program that takes a sentence as input and counts the number of vowels (a, e, i, o, u) 

# take the input from the user
sentance = input('Enter a sentance: ')

# lowering the letters in the sentance
sentance = sentance.lower()
vowels = 0
# checking mechaism for every character in the sentance
for char in sentance:
    if char in ['a', 'e', 'i', 'o', 'u']:
        vowels = vowels +1
        
print(f'No.of vowels in the sentance are {vowels}')
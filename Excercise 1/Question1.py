#Write a Python program that checks if a given year is a leap year or not. A leap year is divisible by 4, but not divisible by 100 unless it is divisible by 400.

# take input of the year from the user

year = int(input('Enter the year: '))

# checking if the year is divisible by 4
if year % 4 == 0:
    # checking if the year is divisible by both 4 and 100
    if year % 100 == 0:
        # checking if the year is divisible by both 4, 100 and 400
        if year % 400 == 0:
            print(f'the {year} is a leap year.')
        else:
            print(f'the {year} is not a leap year')
    else: print(f'the {year} is a leap year')
else:
    print('the {year} is not a leap year')
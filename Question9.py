# Write a program that takes a list of words and returns the longest word(s).

list1 = ['car', 'bike', 'bus']
#  initiating the max length to zero
max_len = 0
# searching for longest length in the word list
for word in list1:
    if len(word) > max_len:
        max_len = len(word)
result = []

# adding the words to reslt if it matches the longest length
for word in list1:
    if len(word) == max_len:
        result.append(word)

print(result)
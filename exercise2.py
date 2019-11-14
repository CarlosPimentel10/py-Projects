# FIND THE NUMBER OF OCCURRENCES OF LETTERS IN THE FOLLOWING STRING
# use a dictionary
# from pprint import pprint -> this module is used to print data in a more readable way
sentence = 'This is a common interview question'
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
# pprint(char_frequency, width=1) -> this function is used to print data in a more readable way

char_frequency_sorted = sorted(char_frequency.items(),
                               key=lambda kv:kv[1],
                               reverse=True)
print(char_frequency_sorted[0])

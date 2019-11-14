# Handle exceptions in python
# input error of alpha instead of integer
"""
try:
    age = int(input('Age: '))
except ValueError as ex:
    print('You did not enter a valid age.')
    print(ex)
    print(type(ex))
else:
    print('No exceptions where thrown')
print('Execution continues')

# Value Error and Zero division error
try:
    age = int(input('Age: '))
    x_factor = 10 / age
except (ValueError, ZeroDivisionError):
    print('You did not enter a valid age.')
else:
    print('No exceptions where thrown')

"""
# Raise exception
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError('Age cannot be 0 or less.')
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

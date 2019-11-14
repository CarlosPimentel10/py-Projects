# fizz_buzz challenge - Solved!
# Create a program that takes an int and slices a string to get
# The fizz if divided by 3, or Buzz if divided by 5
"""
def fizz_buzz(num):
    message = 'FizzBuzz'
    if (num % 3 == 0) and (num % 5 == 0):
        return 'FizzBuzz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    else:
        return 'Something went wrong'


print(fizz_buzz(15))
"""
# Map function with lambda function - to get values from list
from array import array

"""
products = [
    ('Product1', 9),
    ('Product2', 10),
    ('Product3', 14),
    ('Product4', 20)
]
prices = list(map(lambda item: item[1], products))
print(prices)
# List comprehension
filtered = [item for item in products if item[1] >= 10]
print(filtered)
"""
# Zip function to concatenate two lists into one
"""
list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(list(zip('abc', list1, list2)))
"""
# Swapping 2 variables
"""
x = 14
y = 54

x, y = y, x
print('x', x, 'y', y)
"""
from array import array
from sys import getsizeof

numbers = array('i', [1, 2, 3])
print(numbers)
# Set - data type

nums = [1, 2, 3, 4, 5, 6]
first = set(nums)
second = {1, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

if 1 in first:
    print('yes')

# Dictionary

point = {'x': 1, 'y': 2}
point = dict(x=1, y=2)
point['x'] = 10
point['z'] = 20
if 'a' in point:
    print(point['a'])
print(point.get('a', 0))
del point['x']
for key in point:
    print(key, point[key])
# Generator vs list
values = (x * 2 for x in range(100000))
print('gen: ', getsizeof(values))
value_list = [x * 2 for x in range(100000)]
print('list: ', getsizeof(value_list))



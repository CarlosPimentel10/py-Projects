"""
# The standard string repr for dicts is hard to read:
import json

my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
my_mapping
{'b': 42, 'c': 12648430, 'a': 23}  # 😞

# The "json" module can do a much better job:
print(json.dumps(my_mapping, indent=4, sort_keys=True))
{
    "a": 23,
    "b": 42,
    "c": 12648430
}

# Note this only works with dicts containing
# primitive types (check out the "pprint" module):
# print(json.dumps({all: 'yup'}))
# TypeError: keys must be a string
# Why Python is Great: Namedtuples
# Using namedtuple is way shorter than
# defining a class manually:
from collections import namedtuple
Car = namedtuple('Car', 'color mileage')

# Our new "Car" class works as expected:
my_car = Car('red', 3812.4)
my_car.color

'red'
my_car.mileage
3812.4

# We get a nice string repr for free:
my_car
Car(color='red', mileage=3812.4)

# Like tuples, namedtuples are immutable:
my_car.color = 'blue'

"""
# Because Python has first-class functions they can
# be used to emulate switch/case statements


def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    else:
        return None


def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()


dispatch_if('mul', 2, 8)

dispatch_dict('mul', 2, 8)

dispatch_if('unknown', 2, 8)

dispatch_dict('unknown', 2, 8)

# using properties like getters and setters
"""
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative')
        self.__price = value


product = Product(-10)
print(product.price)
"""
# Inheritance


class Animal:
    def __init__(self):
        self.age = 12

    def eat(self):
        print('eat')


class Mammal(Animal):
    def walk(self):
        print('Walk')


class Fish(Animal):
    def swim(self):
        print('Swim')


cat = Mammal()
cat.eat()
print(cat.age)

# Classes
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# define a class method
# Using decorator
    @classmethod
    def zero(cls):
        return cls(0, 0)

# Other magic methods for comparison
# __eq__ tests for equality
# __gt__ tests for > than
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def draw(self):
        print(f'Point ({self.x}, {self.y}')


point = Point(10, 20)
other = Point(1, 5)
print(point == other)

from typing import override
import math

class Shape:

    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    @override
    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @override
    def area(self):
        return self.radius ** 2 * math.pi


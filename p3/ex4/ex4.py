#!/usr/bin/env python3

from collections import namedtuple

class Complex:

    def __init__(self, r, i):
        self.r = r  # store real part in class instance
        self.i = i  # store imaginary part in class instance

    def add(self, y):
        return Complex(self.r + y.r, self.i + y.i)

    def multiply(self, y):
        return Complex(self.r * y.r, self.i + y.i, self.r * y.i, self.i * y.r)

    def __str__(self):
        if(self.i > 0 ):
            return str(self.r) + '+' + str(self.i) + 'i'
        return str(self.r) + '-' + str(self.i) + 'i'


def main():
    # declare two instances of class two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant

    # Test add
    print(c1)  # uses the __str__ method in the class
    c1.add(c2)
    print(c1)  # uses the __str__ method in the class

    # test multiply
    print(c2)  # uses the __str__ method in the class
    c2.add(c1)
    print(c2)  # uses the __str__ method in the class
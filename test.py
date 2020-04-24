#! /bin/python
from numpy import *
# from array import *
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])


def factorial(f):
    if f == 1:
        return f
    return f * factorial(f-1)


fact = 6
print(factorial(fact))

print(__name__)
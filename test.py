#! /bin/python
#from numpy import *
# from array import *
import sys
from Student import *

x = int(sys.argv[1])
y = int(sys.argv[2])


def factorial(f):
    if f == 1:
        return f
    return f * factorial(f-1)

fact = 6
print(factorial(fact))
print(__name__)
st1 = Student("Gunnu", "UKG")
print(st1.school, " : ", st1.getName(), "   ", st1.getCls())
Student.setSchoolName("DAV")
st2 = Student("Sahil", "LKG")
print(st2.school, " : ", st2.getName(), " -- ", st2.getCls())

print("printing sum : ",st2.sum(1))
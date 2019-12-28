#!/usr/bin/python2.7
#-*-coding:Utf-8 -*
# Simple function
def myFunction():
    print("Simple function")

# Calling function
myFunction()

# Function with param
def functionWithParam(a, b, c):
    print(a)
    print(b)
    print("This is the 3rd param: ", c)

functionWithParam(1, 2, " and not three")

# Function with default value for param
def defaultValue(a = 1, b = 2, c = 23):
	print(a)
	print(b)
	print(c)

defaultValue()
defaultValue(c = 25) 

# Function returning a value
def returnValue():
	return 24

r = returnValue()
print(r)

# Function returning many values
def manyValues():
	return 23, 50

a, b = manyValues()
print("First returned value: ", a, " - Second returned value: ", b)

# Function with docstring
def multiply(a, b):
	"""This function has 2 params:
	- a first param
	- b second param
	It returns a value:
	- a * b"""
	return a * b

print(multiply(3, 5))
help(multiply)

# Lambda function
f = lambda x, y : x + y

f(4, 8)

# Import
import math
import math as newNamespaceMath

# Only import 1 fn of a namespace
from math import fabs
fabs(-98)
from math import *

#! /usr/bin/python3.10

from sympy import *
import numpy as np

# get inputs
fun1Var1 = input('What is the first value of the function that requires derivatives F=<\033[4m8t\033[0m,4t^2> ')
print("")
fun1var2 = input('What is the second value of the function that requires derivatives F=<8t,\033[4m4t^2\033[0m> ')
print("")
fun2var1 = input('What is the first value of the vector field function ')
print("")
fun2var2 = input('What is the second value of the vector field function ')

# take derivatives
# This is where the fun begins
x = Symbol('x')
y = Symbol('y')
t = Symbol('t')

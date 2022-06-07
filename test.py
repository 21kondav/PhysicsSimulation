
import numpy as np
from sympy.physics.mechanics import *
from sympy import *
from sympy.physics.vector import *

class Equation:
    def __init__(self, eq):
        self.eq = eq
        x, y, z, t = symbols('x y z t')
        expr = ''
        for char in eq:
            if(char=='x'):
                expr = expr + x
            elif(char =='y'):
                expr = expr + y
            elif(char=='z'):
                expr = expr + z
            elif(char=='t'):
                expr = expr + t
            else:
                expr = expr + char
        self.sympify(expr)
    def fPrime(self, var):
        self = sympify(self)
        var = symbols(var)
        diff(self, var)
    def integral(self, var):
        self = sympify(self)
        var = symbols(var)
        integrate(self, var)

testEq = Equation('x**2 + 2*2')
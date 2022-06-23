import numpy as np
from sympy.physics.mechanics import *
from sympy import *
from sympy.physics.vector import *
#creating vectors and operating
m = Symbol('m')
po = Point('po')
pa = Particle('pa',po, m)
#Building calculus methods
system = {} #a dictionary containing particles and their distance from the center

class Kinematics:
    def __init__(self, N, part, eqMotion):
        N = ReferenceFrame(N)
        self.part = part
        self.eqMotion = eqMotion
    def createEqMot(self, r, v, a):
        self.eqMotion = {'r': r, 'v': v, 'a': a}

class Equation: #creates equation and methods to act on
    def __init__(self, eq):
        x, y, z, t = symbols('x y z t')
        expr = ''
        for char in eq:
            if(char=='x'):
                expr = expr + x
            elif(char=='y'):
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

    def numVar(self, var, a):
        return self.subs(var, a)

class Vector:
    def __init__(self, x, y, z):
        N = ReferenceFrame('N')
        self.x = x
        self.y = y
        self.z = z
        self.vect = [x, y, z]
    def scale(self, comp, n): #scale component
        if comp.equals('x'):
            self.x = self.x *n
        if comp.equals('y'):
            self.y = self.y *n
        if comp.equals('z'):
            self.z = self.z *n
        if comp.equals('r'):
            self.x = self.x * n
            self.y = self.y *n
            self.z = self.z *n 
    def getVect(self):
        return self.vect
    def cross(self, vect2):
        x = self.vect[1]*vect2.vect[2] - self.vect[2]*vect2.vect[1]
        y = self.vect[2]*vect2.vect[0]-self.vect[0]*vect2[2]
        z = self.vect[0]*vect2.vect[3]-self.vect[3]*vect2[0]
        crossed = Vector(x, y, z)
        return crossed
    def dot(self, vect2):
        d = self.vect[0] * vect2.vect[0] + self.vect[1] *vect2.vect[1] +self.vect[2] *vect2.vect[2]
        return d
    def addVect(self, vect2):
        x = self.x + vect2.x
        y = self.y + vect2.y
        z = self.z + vect2.z
        addVect = Vector(x, y, z)
        return addVect
#Calculus on vectors
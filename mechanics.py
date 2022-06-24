import numpy as np
from sympy.physics.mechanics import *
from sympy import *
from sympy.physics.vector import *

# most fundamental to any classical system
m = Symbol('m')  # mass for future use
po = Point('po')  # point
pa = Particle('pa', po, m)  # particle
system = {}  # a dictionary containing particles and their distance from the center

# assumptions for kinematics:
#acceleration is constant
#time is continuous and symmetric
#space is uniform and symmetric
# all events are deterministic
# all positions and velocities are absolute


class Kinematics:  # the backbone for all things kinematic, i.e. when an absolute position, velocity, or acceleration is known
    def __init__(self, N, part, eqMotion):  # creates a kinematic scenario
        # defines a reference for which an object is present in
        N = ReferenceFrame(N)
        self.part = part  # possibly unecesary ------------
        self.eqMotion = eqMotion

    # a set of a equations which defines the motion of any object; the goal for any classical solution to a problem
    def createEqMot(self, r, v, a):
        self.eqMotion = {'Position': r, 'Velocity': v, 'Acceleration': a}

    def getEqMot(self, value):  # Param value: "Position", "Velocity", "Acceleration"
        return self.eqMotion.get(value)

    def addToSystem(self):  # adds to the dictionary system
        pos = self.getEqMot("Position")
        obj = self
        obLocation = {obj: pos}
        system.update(obLocation)


class Equation:  # creates equation and methods to act on
    def __init__(self, eq):
        # defines common symbols (may need updated)
        x, y, z, t = symbols('x y z t')
        expr = ''
        # replaces characters with symbols
        for char in eq:
            if(char == 'x'):
                expr = expr + x
            elif(char == 'y'):
                expr = expr + y
            elif(char == 'z'):
                expr = expr + z
            elif(char == 't'):
                expr = expr + t
            else:
                expr = expr + char
        self.sympify(expr)  # allows sympy to parse the expression

    def fPrime(self, var):  # derivative of self with respect to var
        self = sympify(self)  # possibly unecesary ------------
        var = symbols(var)
        diff(self, var)

    def integral(self, var):  # derivative of self with respect to var
        self = sympify(self)  # possibly unecesary ------------
        var = symbols(var)
        integrate(self, var)

    def numVar(self, var, a):  # substitutes a number for a variable (for solving numerical problems)
        return self.subs(var, a)


class Vector:
    def __init__(self, x, y, z):  # creates a vector
        N = ReferenceFrame('N')
        self.x = x
        self.y = y
        self.z = z
        self.vect = [x, y, z]

    def scale(self, comp, n):  # scale component
        if comp.equals('x'):
            self.x = self.x * n
        if comp.equals('y'):
            self.y = self.y * n
        if comp.equals('z'):
            self.z = self.z * n
        if comp.equals('r'):
            self.x = self.x * n
            self.y = self.y * n
            self.z = self.z * n

    def getVect(self):  # returns vector
        return self.vect

    def cross(self, vect2):  # cross product between self and another vector
        x = self.vect[1]*vect2.vect[2] - self.vect[2]*vect2.vect[1]
        y = self.vect[2]*vect2.vect[0]-self.vect[0]*vect2[2]
        z = self.vect[0]*vect2.vect[3]-self.vect[3]*vect2[0]
        crossed = Vector(x, y, z)
        return crossed

    def dot(self, vect2):  # dot product between self and another vector
        d = self.vect[0] * vect2.vect[0] + self.vect[1] * \
            vect2.vect[1] + self.vect[2] * vect2.vect[2]
        return d

    def addVect(self, vect2):  # addition between self and another vector
        x = self.x + vect2.x
        y = self.y + vect2.y
        z = self.z + vect2.z
        addVect = Vector(x, y, z)
        return addVect
# Calculus on vectors

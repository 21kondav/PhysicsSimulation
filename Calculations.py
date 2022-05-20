import numpy as np
from Sympy import *

#creating vectors and operating
class vectors:
  def __innit__(x, y, z):
    self.x = x
    self.y = y
    self.z = z
  def vector():
    vect = [self.x, self.y, self.z]
    return vec

  def dotProduct(vect1, vect2):
    dp = np.dot(vect1, vect2)
    return  dp
  
  def crossProduct(vect1, vect2):
    cp = np.cross(vect1, vect2)
    return cp
def f(x, y, z, t):
  f = input("What is the fuction")
  return f
#Building calculus methods
class calculus:
  #variable set up
  x, y, z, t = symbols('xyzt')
  #partial derivatives
  def derivative(f):
    ask = input("What do you want to differentiate with respect to?")
    tempf = f
    for i in ask:
      if ask[i].equals('x'):
        rep = input("How many times do you want differentiate with respect to x?")
        count = 1

        while count <= rep:
          tempf = tempf.diff(x)
          count +=1

      elif i.equals('y'):
        rep = input("How many times do you want differentiate with respect to y?")
        count = 1

        while count <= rep:
          tempf = tempf.diff(y)
          count += 1

      elif i.equals('z'):
        rep = input("How many times do you want differentiate with respect to z?")
        count += 1

        while count <= rep:
          tempf = tempf.diff(z)
          count += 1

      elif i.equals('t'):
        rep = input("How many times do you want differentiate with respect to t?")
        count = 1

        while count <= rep:
          tempf = tempf.diff(t)
          count +=  1
    deriv = tempf
    return deriv

  def integral(f):
    tempf = f
    num = input("What do you want to integrate with respect to? Enter in the order you want to integrate (xyzd)")
    
    count = 1
    for i in num: 
      bounds = input(f"Are there any bounds on integration {count}? Type as [lower, upper] type null for each if there are none")
      if bounds[1] != null and bounds[3] != null:
        if i.equals('x'):
          tempf = integrate(tempf, x)

        elif i.equals('y'):
          tempf = integrate(tempf, y)

        elif i.equals('z'):
          integrate(tempf, 'z')
          
        elif i.equals('t'):
          integrate(tempf, 't')
      integ = tempf
      return integ

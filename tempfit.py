#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x=[90,60,30,20]
y=[15,18,30,42]

angle=90-np.array(x) #in degrees
angrad= angle*np.pi/180 #in radians
T_A=200 #kelvin

def func(x, a):
  return T_A*(1-np.exp(-a/np.cos(angrad)))

p0=sy.array([1])  
coeffs, matcov = curve_fit(func, x, y, p0)

yaj = func(x, coeffs[0])
print(coeffs)
print(matcov)

plt.plot(x,y,'ko',x,yaj,'b-')
plt.xlabel('Elevation angle (degrees)')
plt.ylabel('Temperature (K)')
plt.show()


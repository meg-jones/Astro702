#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from pylab import *
import scipy as sy


v = np.array([224,218,228,237,255,251,250,256,270,271,263,261,261])
ve = [1,10,4,6,3,4,11,18,7,12,7,11,11]
R = [2.44,2.99,3.52,4.04,4.54,5.01,5.46,5.89,6.29,6.65,6.99,7.29,7.55]
Re = [0.10,0.13,0.15,0.17,0.19,0.21,0.23,0.25,0.26,0.28,0.29,0.31,0.32]
n_HI = [1.8364,2.1909,1.8625,2.0782,1.8213,1.8358,1.7352,1.3539,1.6609,1.3530,1.1390,1.1349,1.0876]
G = 4.302e-6 #kpc/M_o (km/s)**2

M = v**2*R/G/10**11
v0=251
R0=8.33
v_keplerian = np.sqrt(R0)*v0*np.sqrt(1/np.array(R))
v_solid = v0/R0*np.array(R)



plt.plot(R,v,'kx')
plt.plot(R,v_keplerian,'k-', R,v_solid,'k--')
plt.xlabel("Radial Distance (kpc)")
plt.ylabel("Velocity (km/s)")
plt.errorbar(R,v,yerr=ve, xerr=Re,fmt=None)
plt.show()

plt.plot(R,n_HI,'kx')
plt.xlabel(r"Number Density of HI (cm$^{-3}$)")
plt.ylabel("Velocity (km/s)")
plt.errorbar(R,n_HI,xerr=Re,fmt=None)
plt.show()

plt.plot(R,M,'kx')
plt.xlabel("Radial Distance (kpc)")
plt.ylabel(r"Mass (10$^{11}$ M$_{\odot}$)")
#plt.errorbar(R,n_HI,xerr=Re,fmt=None)
plt.show()


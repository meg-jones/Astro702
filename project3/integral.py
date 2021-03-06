#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from pylab import *
import scipy as sy


try:
    lon = sys.argv[1]
    freq,temperature = np.loadtxt('lon'+lon+'.dat',unpack=True, usecols=(0,1))
except IndexError:
	print "file not read" % sys.argv[0]
	sys.exit(1)

l = int(float(lon))
v0=251.0 #km/s
f0=1420.4 #MHz
c=3.0e5 #km/s

vel=(f0-freq)*c/f0+v0*sin(pi*l/180.0)
sum_T = sum(temperature)
dv = abs(vel[1] - vel[0])
n_HI = 1.8224e18*sum_T*dv

R0 = 8.33 #kpc
R = R0*sin(pi*l/180.0)
Re = 0.35*sin(pi*l/180.0)

print lon
#print n_HI
#print R
print Re



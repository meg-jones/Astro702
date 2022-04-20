#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from pylab import *
import scipy as sy

#defining constants
T=np.arange(1e5,1e8,100)
Z=0.02
Y=0.28
X=0.7
r=10
R=1e4
mu_e=2/(1+X)
mu_I=1/(X+Y/4+Z/16)

#radiative opacities for r
K_bf=4e25*Z*(1+X)*r*T**-3.5	
K_ff=1e23*r*Z**2*T**-3.5/(mu_e*mu_I)	
#K_H=2.5e-31*(Z/0.02)*sqrt(r)*T**9	

#total opacity
K=K_bf+K_ff

#radiative opacities for R
K_bf_2=4e25*Z*(1+X)*R*T**-3.5
K_ff_2=1e23*R*Z**2*T**-3.5/(mu_e*mu_I)
#K_H_2=2.5e-31*(Z/0.02)*sqrt(R)*T**9

#total opacity
K2=K_bf_2+K_ff_2

#conductive opacities
K_c=4e-8*mu_e**2/mu_I*Z**2*T**2/r**2
K_c_2=4e-8*mu_e**2/mu_I*Z**2*T**2/R**2

#total opacities (radiative + conductive)
K_tot=1/(1/K+1/K_c)
K_tot2=1/(1/K2+1/K_c_2)

#it's plotting time!
plt.plot(T,K,label='density=10 g/cm$^{3}$')
plt.plot(T,K2,label='density=10$^{4}$ g/cm$^{3}$')
plt.plot(T,K_tot,label='density=10 g/cm$^{3}$')
plt.plot(T,K_tot2,label='density=10$^{4}$ g/cm$^{3}$')
plt.legend(loc='best')
plt.loglog()
plt.xlabel("Temperature (K)")
plt.ylabel("Opacity (cm$^{2}$/g)")
plt.title('Total Opacity')
plt.show()


#!/usr/env/python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

A=0.109082976 #fraction of sky
T=0.003125 #days


R=np.linspace(0,50000,50000)
p_R=(A*T)**4*R**4*np.exp(-R*A*T)
norm_p_R = p_R/max(p_R)


#p_R peaks at R=11734.161734161735

#from looking at plot of posterior density function, only need to integrate out to R=50000

posterior = lambda x: (A*T)**4*x**4*np.exp(-x*A*T)
norm = quad(posterior, 0, 50000)
norm = norm[0]

integrand = lambda x: (A*T)**4*x**5*np.exp(-x*A*T)
R1 = quad(integrand, 0, 50000)
R1 = R1[0]
Ravg = R1/norm


#Integrate posterior
Rlist=[]
for i in range(1,50001):
	integrand = lambda x: x*(A*T)**4*x**4*np.exp(-x*A*T)
	R2 = quad(integrand, 0, i)
	Ravg = R2[0]
	Rlist.append(Ravg)

Rlist2 = Rlist/max(Rlist)

#Find lower limit on 95% confidence
for l in range(0,len(Rlist2)):
	if Rlist2[l] >= 0.025:
		lower = R[l]
		break
#Find upper limit on 95% confidence
for m in range(0,len(Rlist2)):
	if Rlist2[m] >= 0.975:
		upper = R[m]
		break

normalize=[]
for n in range(0, len(norm_p_R)):
	if R[n]>=lower and R[n]<=upper:
		normalize.append(norm_p_R[n])

x1 = [lower, lower]
y1 = [0, normalize[0]]
x2 = [upper, upper]
y2 = [0, normalize[25251]]

plt.plot(R,norm_p_R,'k-')
plt.plot(x1,y1,'b--', x2, y2, 'b--')
plt.xlabel('${\cal R}$ (FRBs day$^{-1}$)')
plt.ylabel('Posterior Probability Density Function')
plt.show()

plt.plot(R,Rlist2,'k-')
plt.show()

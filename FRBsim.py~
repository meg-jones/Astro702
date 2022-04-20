#!/usr/env/python
import numpy as np
import matplotlib.pyplot as plt
import scipy as sy
from scipy.optimize import curve_fit
from math import exp
from scipy.integrate import quad

Dmax = 7.8 #Gpc

#The values as found by that fit are below.
#a=0.0304 #0.134
#b=0.8884 #3.920
#c=-0.1826 #-0.806
#d=0.01514 #0.0667
#Dtest=(a+b*z+c*z**2+d*z**3)*3e2/68

luminosity = []
DM = []
flux = []
sigma = 4.67 #calculated from equation in class

#Model A
num1 = []
num = []
data = np.loadtxt('observed.FRBs')
DMobs, fluxobs = [],[]
for a in range(0,len(data)):
	DMobs.append(data[a][0])
	fluxobs.append(data[a][1])
probsum=[]
filename='FRBsim3.txt'
file=open(filename,'w')

for p in range(50,260,10): #Lsigma
	for l in range(50,260,10): #Lmean
		for k in range(0,10000,1):
        		lr = np.random.normal(0,1)
        		L = lr*p+l
        		r = np.random.uniform(0,1)
        		D = Dmax*r**0.333333
        		z=0.026+0.14*D+0.072*D**2-0.014*D**3+0.0016*D**4
        		S = L/(4*np.pi*D**2*(1+z)**2)
        		beamsize = np.random.uniform(0,1)*5.5
        		flux.append(np.exp(-beamsize**2/(2*sigma**2))*S)
        		luminosity.append(L)
        		DM.append(25+1200*z+150)
                prob=0
		for j in range (0,len(DMobs)):		
			a=1
                	for h in range(0,len(DM)):
				if abs(DM[h]-DMobs[j]) <= 0.1*DMobs[j] and abs(flux[h]-fluxobs[j]) <= 0.1*fluxobs[j]:
					a+=1
			prob+=np.log10(a/100000.0)				
#		probsum.append(prob)
		print p, l, prob,
                file.write(str(p)+'  '+str(l)+'  '+str(prob)+'\n')          
file.close()

		
#print len(luminosity)
#print len(flux)
#print len(DM)
#print len(probsum)

#for m in range(0,len(DM)): 
#    file.write(str(luminosity[m])+'  '+str(DM[m])+'  '+str(flux[m])+'  '+str(probsum[m])+'\n')
#file.close()

#plt.plot(DM,flux,'k+')
#plt.plot(DMobs,fluxobs,'ro')
#plt.xlabel(r'DM (pc cm$^{-3}$) ')
#plt.ylabel('Flux Density')
#plt.yscale('log')
#plt.xscale('log')
#plt.show()

#cat FRBsim.txt |awk '{print $1,$2,10**(33+$3)}' > meowstubh.cat

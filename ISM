import numpy as np
import matplotlib.pyplot as plt

number=5000
constant=number/1.888
Masses=np.arange(0.5,100,1)
Temperature=Masses**(7./12)*5800
h=6.626*10**(-27)
k=1.38*10**(-16)
nu=np.arange(4,20,0.1)
nu=10**nu
c=3*10**10

def B(T):
    return 2*h*nu**3/(c**2*(np.exp(h*nu/(k*T))-1))

N=[]
for i in range(0,len(Masses)-1):
    N.append(constant*1/1.35*((Masses[i])**-1.35-(Masses[i+1])**-1.35))

Spectrum=0
for i in range(0,len(Temperature)):
    Spectrum=Spectrum+N[i]*B(Temperature[i])

Line1=N[0]*B(Temperature[0])
Line2=N[49]*B(Temperature[49])

x=[7.5*10**14, 7.5*10**14]
y=[10**-23, 10**5]
x2=[4*10**13, 4*10**13]
x3=[6*10**16, 6*10**16]

plt.plot(nu,Spectrum,'k--',label='Cluster Spectrum')
plt.loglog()
plt.xlabel('Frequency (Hz)')
plt.ylabel('Intensity (erg s$^{-1}$ Hz$^{-1}$ Sr$^{-1}$ cm$^{-2}$)')
plt.xlim(10**12,10**18)
plt.ylim(10**-22,100000)
plt.minorticks_on()
plt.title('Integrated Spectrum of 5,000 stars')
# plt.plot(nu,Line1,'r',label='1 Solar Mass Contribution')
# plt.plot(nu,Line2,'k',label='50 Solar Mass Contribution')
# plt.legend(loc=0)
plt.plot(x,y)
plt.plot(x2,y)
plt.plot(x3,y)

plt.show()

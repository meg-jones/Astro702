import numpy as np
import matplotlib.pyplot as plt

# at all R, V(R)=220 km/s, R_o=8 kpc
# R=4, 6, 10, 12 kpc
# 0>phi>2*pi

R0=8
R1=4
R2=6
R3=10
R4=12
V=220
V0=220
phi=np.arange(0,2*3.14159,3.14159/180)

#1st ring
d1=np.sqrt(R1**2+R0**2-2*R1*R0*np.cos(phi))
cosl1=((R0-R1*np.cos(phi))/np.sqrt(R0**2+R1**2-2*R0*R1*np.cos(phi)))
l1rad=np.arccos(cosl1)
l1=l1rad*180/3.14159

Vlsr1=R0*np.sin(l1rad)*(V/R1-V0/R0)

#2nd ring
d2=np.sqrt(R2**2+R0**2-2*R2*R0*np.cos(phi))
cosl2=((R0-R2*np.cos(phi))/np.sqrt(R0**2+R2**2-2*R0*R2*np.cos(phi)))
l2rad=np.arccos(cosl2)
l2=l2rad*180/3.14159

Vlsr2=R0*np.sin(l2rad)*(V/R2-V0/R0)

#3rd ring
d3=np.sqrt(R3**2+R0**2-2*R3*R0*np.cos(phi))
cosl3=((R0-R3*np.cos(phi))/np.sqrt(R0**2+R3**2-2*R0*R3*np.cos(phi)))
l3rad=np.arccos(cosl3)
l3=l3rad*180/3.14159

Vlsr3=R0*np.sin(l3rad)*(V/R3-V0/R0)

#4th ring
d4=np.sqrt(R4**2+R0**2-2*R4*R0*np.cos(phi))
cosl4=((R0-R4*np.cos(phi))/np.sqrt(R0**2+R4**2-2*R0*R4*np.cos(phi)))
l4rad=np.arccos(cosl4)
l4=l4rad*180/3.14159

Vlsr4=R0*np.sin(l4rad)*(V/R4-V0/R0)

plt.gca().invert_xaxis()
plt.plot(l1,Vlsr1,'b-')
plt.plot(-l1,-Vlsr1,'b-',label='R=4 kpc')
plt.plot(l2,Vlsr2,'r-')
plt.plot(-l2,-Vlsr2,'r-',label='R=6 kpc')
plt.plot(l3,Vlsr3,'g-')
plt.plot(-l3,-Vlsr3,'g-',label='R=10 kpc')
plt.plot(l4,Vlsr4,'k-')
plt.plot(-l4,-Vlsr4,'k-',label='R=12 kpc')
plt.xlabel('Galactic Longitude')
plt.ylabel('V$_{LSR}$ (km/s)')

#plt.legend(loc=0)
plt.show()



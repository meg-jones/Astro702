#!/usr/env/python
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import math

#Simulate noise
r = np.random.normal(0,1,66000) #random noise 
t = np.arange(0.001,66.001,0.001) #time sampling every 1ms

print len(t)

#Generate square-wave
sig = signal.square(2*np.pi*10*t, duty = 0.05) #where 10 Hz is the frequency
sig2=(sig+1)*2.5
#Simulated data
data = r+sig

#Lomb-Scargle Periodogram
freqs = np.linspace(6.28,6.28*1000,4000)
pgram = signal.lombscargle(t,data,freqs)

max_pgram = max(pgram)
max_freqs = freqs[pgram.argmax()]
period = 2*np.pi/freqs
max_period = 2*np.pi/max_freqs

fap = 1-(1-e**(-pgram))**66000

frequency=freqs/(2*np.pi)

plt.plot(t, sig+1)
plt.plot(t,r)
plt.xlim([0,1])
plt.ylabel('Power')
plt.xlabel("Time (s)")
plt.show()

plt.plot(t, data+1)
plt.xlim([0,1])
plt.ylabel('Power')
plt.xlabel("Time (s)")
plt.show()

plt.plot(frequency, pgram)
plt.ylabel('Power')
plt.xlabel("Frequency (Hz)")
plt.xlim([0,100])
plt.ylim([0,50])
plt.show()

#Print to file to open in gnuplot
filename='test.txt'
file=open(filename,'w')
for i in range(0,len(t)):
    file.write(str(t[i])+"  "+str(r[i])+"  "+str(sig[i])+"  "+str(freqs[i]+"  "+str(pgram[i])+"\n")
file.close()

#Harmonics
#9.98816
#19.9756
#29.9631
#39.9452
#48.9461




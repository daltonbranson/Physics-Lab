#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

def rule4(Q, Ae, Be, Aun, Bun, A, B):
    Qun = np.abs(Q)*np.sqrt(((Ae*Aun/A)**2)+((Be*Bun/B)**2))
    return Qun

def stdun(x):
    stdun = np.std(x)/np.sqrt(x.size)
    return stdun


# In[10]:


#Variables, V=volts, T=seconds, c=charge, d=discharge

#Part 1, 12 values per array.
Vcplot = np.array([0, 3.647, 6.128, 7.84, 8.91, 9.67, 10.19, 10.56, 10.81, 10.99, 11.12, 11.21, 11.27])
Tcplot = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

Vdplot = np.array([11.40, 8.04, 5.54, 3.872, 2.669, 1.872, 1.294, .916, .645, .453, .326, .235, .170])
Tdplot = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

#Part 2, 10 values per array.
Vo = 11.45

Tc = np.array([26.75, 26.44, 26.72, 26.86, 26.21, 26.50, 26.32, 26.47, 26.23, 26.35])

Td = np.array([27.70, 27.15, 27.75, 27.86, 28.15, 27.85, 27.38, 27.49, 27.4, 26.93])

#Part 3
Ohms = 502.8e3
Ohm_un = .05e3
Farads = 54.0e-6
Farad_un = .05e-6


# In[11]:


#Part 1
plt.plot(Tcplot, Vcplot); plt.ylabel('Voltage (volts)'); plt.xlabel('Time (seconds)'); plt.title('Charging Capacitor')
plt.show()

plt.plot(Tdplot, Vdplot); plt.ylabel('Voltage (volts)'); plt.xlabel('Time (seconds)'); plt.title('Discharging Capacitor')
plt.show()


# In[12]:


#Part 2
Vc_theoretical = .632*Vo
Vd_theoretical = .368*Vo

Tc_avg = np.mean(Tc); Tc_avgun = stdun(Tc)
Td_avg = np.mean(Td); Td_avgun = stdun(Td)

#print('Our theoretical values for voltage after one time constant when charging and discharging were, respectively,', '%.2f' % Vc_theoretical,'and\
#', '%.2f' % Vd_theoretical,'.')
print('Our average charge time to', '%.2f' % Vc_theoretical, ' volts was', '%.2f' % Tc_avg, '+/-', '%.2f' % Tc_avgun,'seconds.\nOur average discharge time to', '%.2f' % Vd_theoretical, 'volts was', '%.2f' % Td_avg, '+/-', '%.2f' % Td_avgun, 'seconds.' )

#Part 3
Tconstant = (Ohms * Farads); Tconstant_un = rule4(Tconstant, 1, 1, Ohm_un, Farad_un, Ohms, Farads)

print('\nOur theoretical time constant was', '%.2f' % Tconstant, '+/-', '%.2f' % Tconstant_un, 'seconds.')


# In[ ]:





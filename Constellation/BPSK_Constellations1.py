# -*- coding:utf-8 -*-
 
import numpy as np
from math import pi
import matplotlib.pyplot as plt
import math

#-------------------------------------#
#---------- Configuration ------------#
#-------------------------------------#


num_symbols = 2 ** 4

sampling_f = 2 ** 8
sampling_t = 1/sampling_f


t = np.arange(0, num_symbols, sampling_t)
 

# Generate Random signal sequence
a = np.random.randint(0, 2, num_symbols)
m = np.zeros(len(t), dtype=np.float32)

for i in range(len(t)):
    digital_noise = np.random.randn() * 0.04
    m[i] = a[math.floor(t[i])] + digital_noise

# Generate Carrier wave
fc = 2**2 # carrier frequency
carrier_wave = np.cos(np.dot(2 * pi * fc, t))

#analog_noise = np.random.randn(len(coherent_carrier)) * 0.0

# Generate BPSK signal
bpsk = np.cos(np.dot(2 * pi * fc, t) + pi * (m - 1) + 0*pi / 4) # + analog_noise


fig1 = plt.figure(figsize = (6,6), facecolor='lightblue')
ax11 = fig1.add_subplot(3, 1, 1)
ax12 = fig1.add_subplot(3, 1, 2)
ax13 = fig1.add_subplot(3, 1, 3)

ax11.set_title('generate Random Binary signal', fontsize = 16)
ax11.axis([0, num_symbols, -2.5, 4.5])
ax11.plot(t, m, 'b')


ax12.set_title('Carrier Wave', fontsize=16) #, fontproperties=zhfont1
ax12.axis([0,num_symbols,-1.5, 1.5])
ax12.plot(t, carrier_wave, 'r')

ax13.set_title('BPSK Modulation', fontsize=16) #, fontproperties=zhfont1
ax13.axis([0,num_symbols,-1.5, 1.5])
ax13.plot(t, bpsk, 'r')


fig2 = plt.figure(figsize = (6,6), facecolor='lightblue')
ax21 = fig2.add_subplot(2, 1, 1)
ax21.plot(np.real(m), np.imag(m), '.')

plt.show()
print()

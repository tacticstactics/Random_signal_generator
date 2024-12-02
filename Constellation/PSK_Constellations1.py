import numpy as np
import matplotlib.pyplot as plt
import math

fig1 = plt.figure(figsize = (6,8), facecolor='lightblue')
fig1.suptitle('PSK Modulation 1/2', fontsize=12)

ax11 = fig1.add_subplot(3, 1, 1)
ax12 = fig1.add_subplot(3, 1, 2)
#ax13 = fig1.add_subplot(3, 1, 3)

fig2 = plt.figure(figsize = (6,8), facecolor='lightblue')
fig2.suptitle('PSK Modulation 2/2', fontsize=12)
ax21 = fig2.add_subplot(3, 1, 1)
ax22 = fig2.add_subplot(3, 1, 2)
ax23 = fig2.add_subplot(3, 1, 3)

fig3 = plt.figure(figsize = (6,8), facecolor='lightblue')
fig3.suptitle('PSK Modulation 2/2', fontsize=12)
ax31 = fig3.add_subplot(4, 1, 1)
ax32 = fig3.add_subplot(4, 1, 2)
ax33 = fig3.add_subplot(4, 1, 3)
ax34= fig3.add_subplot(4, 1, 4)


num_symbols = 2 ** 4

# Number
sampling_t = 0.01
sampling_f = 1/sampling_t

t = np.arange(0, num_symbols, sampling_t)

#multi level
#ml = 2 # for BPSK
ml = 4 # for QPSK
#ml = 8 # for 8PSK

# Generate Random signal sequence
a = np.random.randint(0, ml, num_symbols)
m = np.zeros(len(t))

noise_amplitude = 0.02

for i in range(len(t)):
    digital_noise = np.random.randn() * noise_amplitude
    m[i] = a[math.floor(t[i])] + digital_noise

#math.floor: 小数点以下を切り捨てる

#x_int = np.random.randint(0, 4, num_symbols) # 0 to 3
x_int = m

offset_degree = 360 / (ml * 2)

x_degrees = x_int*360/ml + offset_degree # 45, 135, 225, 315 degrees

x_radians = x_degrees*np.pi/180.0 # sin() and cos() takes in radians

#1
ax11.plot(a, marker="o")
ax12.plot(t,x_radians)



x_symbols = np.cos(x_radians) + 1j*np.sin(x_radians) # this produces Quadrature Phase Shift Keying(QPSK) complex symbols


#n = (np.random.randn(num_symbols) + 1j*np.random.randn(num_symbols))/np.sqrt(2) # Additive white Gaussian noise(AWGN) with unity power

#noise_power = 0.01

#phase_noise = np.random.randn(len(x_symbols)) * 0.1 # adjust multiplier for "strength" of phase noise

#r = x_symbols * np.exp(1j*phase_noise) + n * np.sqrt(noise_power)

#1



ax21.plot(np.real(x_symbols), np.imag(x_symbols), '.')
ax21.grid(True)

ax21.set_xlabel('Inphase [V]')
ax21.set_ylabel('Quadrature [V]')

ax22.plot(t, np.real(x_symbols))
ax23.plot(t, np.imag(x_symbols))


I_signal = np.cos(x_radians)
Q_signal = np.sin(x_radians)

# Generate Carrier wave
fc = 2**1 # carrier frequency
carrier1 = np.cos(np.dot(2 * np.pi * fc, t))
carrier2 = np.cos(np.dot(2 * np.pi * fc, t))

ax32.set_title('Carrier Wave', fontsize=16) #, fontproperties=zhfont1
ax32.plot(t, carrier1, 'r')


#analog_noise = np.random.randn(len(coherent_carrier)) * 0.0

I_signal_modulated = np.cos(np.dot(2 * np.pi * fc, t) + np.pi * (I_signal - 1) + np.pi / 4) # + analog_noise

Q_signal_modulated = np.cos(np.dot(2 * np.pi * fc, t) + np.pi * (Q_signal - 1) + np.pi / 4) # + analog_noise

ax33.plot(t, I_signal_modulated, 'r')
ax34.plot(t, Q_signal_modulated, 'r')

plt.show()
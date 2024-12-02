
import numpy as np
import matplotlib.pyplot as plt
import math

num_symbols = 2 ** 12
sampling_t = 0.01

t = np.arange(0, num_symbols, sampling_t)

# Generate Random signal sequence
a = np.random.randint(0, 4, num_symbols)
m = np.zeros(len(t))

for i in range(len(t)):
    digital_noise = np.random.randn() * 0.04
    m[i] = a[math.floor(t[i])] + digital_noise

x_int = np.random.randint(0, 8, num_symbols) # 0 to 7 for 8-PSK

x_degrees = x_int*360/8 + 0 # 45, 90, 135, 180, 225, 270, 315, 360 degrees

x_radians = x_degrees*np.pi/180 # sin() and cos() takes in radians

x_symbols = np.cos(x_radians) + 1j*np.sin(x_radians) # this produces our Quadrature Phase Shift Keying(QPSK) complex symbols

n = (np.random.randn(num_symbols) + 1j*np.random.randn(num_symbols))/np.sqrt(2) # Additive white Gaussian noise(AWGN) with unity power

noise_power = 0.001

phase_noise = np.random.randn(len(x_symbols)) * 0.001 # adjust multiplier for "strength" of phase noise

r = x_symbols * np.exp(1j*phase_noise) + n * np.sqrt(noise_power)

fig1 = plt.figure(figsize = (5,8), facecolor='lightblue')
ax1 = fig1.add_subplot(2, 1, 1)
ax2 = fig1.add_subplot(2, 1, 2)

ax1.plot(np.real(x_symbols), np.imag(x_symbols), '.')
ax2.plot(np.real(r), np.imag(r), '.')

fig2 = plt.figure(figsize = (5,8), facecolor='lightblue')

ax21 = fig2.add_subplot(2, 1, 1)
ax22 = fig2.add_subplot(2, 1, 2)
ax21.plot(np.real(r),'.')
ax22.plot(np.imag(r),'.')

plt.show()

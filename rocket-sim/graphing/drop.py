import math
import numpy as np
import matplotlib.pyplot as plt

# https://stackoverflow.com/questions/71542662/python-plotting-free-fall-with-drag

mass = 3  # kg
g = 9.81    # m/s/s
c_1 = 1.75
rho_0 = 1.229
h_n = 10400
area = 0.5
dt = 0.01     # reduce delta t to improve computation speed (result not impacted)
t = np.arange(0, 20, dt)  # extend time to 600 seconds

x = np.zeros(len(t))
v = np.zeros(len(t))
a = np.zeros(len(t))
rho = np.zeros(len(t))

x[0] = 100
v[0] = 0
a[0] = -g

for i in range(1, len(t)):
    rho[i] = rho_0 * np.exp(-x[i-1]/h_n)
    a[i] = -g + c_1*rho[i]*area*(v[i-1]**2)/mass
    v[i] = v[i-1] + a[i-1]*dt
    x[i] = x[i-1] + v[i-1]*dt


f, (ax1, ax2, ax3) = plt.subplots(3,1,sharex=True,figsize=(8,12))
ax1.plot(t, x)
ax1.set(ylabel = 'Altitude (m)')
ax1.grid()

ax2.plot(t, v)
ax2.set(ylabel = 'Velocity (m/s)')
ax2.grid()

ax3.plot(t, a)
ax3.set(ylabel = 'Acceleration (m/s/s)', xlabel = 'Time (secs)')
ax3.grid()

plt.show()

print("done")
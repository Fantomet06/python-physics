import math
import numpy as np
import matplotlib.pyplot as plt

rho = 1.229 #density of air in kg/m^3
g = 9.81 #acceleration due to gravity in m/s^2
Cd = 0.5 #drag coefficient of rocket
m = 1 #mass of rocket in kg
A = 0.0078 #area of rocket in m^2
V = 8.7 #velocity of rocket in m/s
F = 8.7*2 #force of rocket engine in N

dt = 0.01     # reduce delta t to improve computation speed (result not impacted)
t = np.arange(0, 2.9, dt)  # extend time to 600 seconds

y = []
vel = []
time = [0]

x = np.zeros(len(t))
v = np.zeros(len(t))
a = np.zeros(len(t))
x[0] = 0
v[0] = F-(0.5*rho*(F**2)*Cd*A+g)
a[0] = F-(0.5*rho*(F**2)*Cd*A+g)/m

#running time for fuel: 2.9 seconds

for i in range(1, len(t)):
    a[i] = F-(0.5*rho*(v[i-1]**2)*Cd*A+g)/m
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
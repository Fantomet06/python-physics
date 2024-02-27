#import math

# 10 pixels = 1 meter

"""
W = 60 #weight of payload in kg
Cd = 1.75 #drag coefficient of parachute
r = 1.229 #density of air in kg/m^3
A = 8.3 #area of parachute in m^2
"""
"""
g = 9.81 #acceleration due to gravity in m/s^2

def velocity(W, Cd, r, A):
    return math.sqrt((2 * W * g)/(Cd * r * A))

def get_area(W, Cd, r, V):
    return (2*W*g)/(Cd*r*V**2)

# given newtons of upward force, calculate the acceleration of the rocket with drag
# https://socratic.org/questions/how-fast-will-an-object-with-a-mass-of-15-kg-accelerate-if-a-force-of-72-n-is-co
def acceleration(W, Cd, r, A, F):
    return (F - (0.5 * Cd * r * A * V**2))/W

#print(velocity(W, Cd, r, A))
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def trajectory(Start_Cd, Parachute_Cd, Mass, Area, Parachute_A, Force, Engines, Time):
    rho = 1.229 #density of air in kg/m^3
    g = 9.81 #acceleration due to gravity in m/s^2
    Cd = Start_Cd
    m = Mass
    A = Area #0.0078 #area of rocket in m^2
    F = Force * Engines #8.7*2 #force of rocket engine in N

    dt = 0.01     # reduce delta t to improve computation speed (result not impacted)
    t = np.arange(0, 50, dt)  # extend time to 600 seconds
    # 5.49 

    y = []
    vel = []
    time = [0]

    x = np.zeros(len(t))
    v = np.zeros(len(t))
    a = np.zeros(len(t))
    x[0] = 0
    v[0] = (F-(0.5*rho*(F**2)*Cd*A+g))*dt
    a[0] = (F-(0.5*rho*(F**2)*Cd*A+g)/m)*dt

    #running time for fuel: 2.9 seconds

    for i in range(1, len(t)):
        if t[i] > 0.04 and x[i-1] <= 0:
            break

        if t[i] > 0.01 and v[i-1] <= 0:
            Cd = Parachute_Cd #1.75 #drag coefficient of parachute
            A = Parachute_A #0.5

            a[i] = (-g*m + 0.5*rho*(abs(v[i-1]**2))*Cd*A)/m
            #print(a[i])
            v[i] = v[i-1] + a[i-1]*dt
            x[i] = x[i-1] + v[i-1]*dt

        else:
            if t[i] > Time:
                F = 0

            a[i] = (F-(0.5*rho*(v[i-1]**2)*Cd*A+g))/m
            v[i] = v[i-1] + a[i-1]*dt
            x[i] = x[i-1] + v[i-1]*dt

    #print(x)
    return x
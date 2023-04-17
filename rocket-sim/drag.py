import math

# 10 pixels = 1 meter

"""
W = 60 #weight of payload in kg
Cd = 1.75 #drag coefficient of parachute
r = 1.229 #density of air in kg/m^3
A = 8.3 #area of parachute in m^2
"""
g = 9.81 #acceleration due to gravity in m/s^2

def velocity(W, Cd, r, A):
    return math.sqrt((2 * W * g)/(Cd * r * A))

def get_area(W, Cd, r, V):
    return (2*W*g)/(Cd*r*V**2)

#print(velocity(W, Cd, r, A))
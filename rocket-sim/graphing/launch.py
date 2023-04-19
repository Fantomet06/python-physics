import math

rho = 1.229 #density of air in kg/m^3
g = 9.81 #acceleration due to gravity in m/s^2
Cd = 1.75 #drag coefficient of rocket
m = 3 #mass of rocket in kg
A = 0.5 #area of rocket in m^2
V = 0 #velocity of rocket in m/s
F = 0 #force of rocket engine in N

Ft = (F-(0.5*rho*(V**2)*Cd*A+g))

a = Ft/m
import math
from numpy import sin, arcsin, cos, arccos, tan, arctan

def distance(x1, z1, x2, z2):
    return ((x2-x1)**2 + (z2-z1)**2)**0.5

def vinkle(opposite, adjancent, k):
    k= abs(k)
    l = float(opposite/adjancent)
    o = math.degrees(math.atan(l))

    return 180-o-k

def pythagoras(hypothenus, angle):
    delta_a = 90 - abs(angle)

    b = hypothenus * math.cos(math.degrees(delta_a))
    a = math.sqrt(hypothenus**2 - b**2)

    return a, b

def triangulate():
    #Det fyrste kastet (defaultverdi til testing)
    x1 = -21
    z1 = 11
    f1 = -28.6

    #Det andre kastet (defaultverdi til testing)
    x2 = -12
    z2 = 6
    f2 = 18.6

    avstand = distance(x1, z1, x2, z2)
    vinkel1 = vinkle(abs(z1-z2), abs(x1-x2), f2)
    vinkel2 = vinkle(abs(x1-x2), abs(z1-z2), f2)

    vinkel3 = 180 - vinkel1 - vinkel2
    c = (avstand * sin(math.radians(vinkel1))) / sin(math.radians(vinkel3))

    print(pythagoras(c, f1))

    return abs(c)

print(triangulate())



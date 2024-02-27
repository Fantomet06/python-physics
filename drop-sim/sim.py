import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('./drop-sim/data.txt')
time = data[:,0]
pos = data[:,1]

pos2 = [3]

k = 0.45

F = 0.05*9.81-k # F = mg

for i in range(len(time)-1):
    pos2.append(pos[i]-F)

print(len(pos2))

plt.figure(1)
plt.plot(time, pos)
plt.plot(time, pos2)
plt.show()
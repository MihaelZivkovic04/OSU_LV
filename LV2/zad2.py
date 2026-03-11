import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data.csv', skiprows=1, delimiter=',')

#print(data.shape)

#mass = data[:, 2]
#height = data[:, 1]

ind = (data[:,0] == 0)

mass = data[ind, 2]
height = data[ind, 1]

#print(mass.shape)
print(height.min(), height.max(), height.mean())

plt.scatter(height, mass)
plt.show()

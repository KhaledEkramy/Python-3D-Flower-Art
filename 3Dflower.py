import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n = 800
p = np.pi

R, T = np.meshgrid(np.linspace(0, 1, n), np.linspace(-2, 20 * p, n))

x = 1 - (0.5) * ((5 / 4) * (1 - (3.6 * T % (2 * p)) / p) ** 2 - 0.25) ** 2
U = 2 * np.exp(-T / (8 * p))
L = np.sin(U)
J = np.cos(U)
y = 1.99 * (R ** 2) * (1.2 * R - 1) ** 2 * L

K = x * (R * L + y * J)
X = K * np.sin(T)
Y = K * np.cos(T)
Z = x * (R * J - y * L)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, facecolors=plt.cm.jet(Z / np.max(Z)), rstride=1, cstride=1, linewidth=0, antialiased=False)

ax.grid(False)
ax.axis('off')

plt.show()

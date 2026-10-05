import matplotlib.pyplot as plt
import numpy as np
def hom2d(theta, tx, ty):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s, tx],[s, c, ty],[0, 0 ,1]])
square = np.array([[0,1,1,0],[0,0,1,1],[1,1,1,1]])
theta1 = np.pi/4
tx1, ty1 = 2.0, 1.0
theta2 = -np.pi/6
tx2, ty2 = -1.0, 3.0
T1 = hom2d(theta1, tx1, ty1)
T2 = hom2d(theta2, tx2, ty2)
rotsq = T1 @ square
tchain = T2 @ T1
chainsq = tchain @ square
plt.figure(figsize=(8,8))
plt.plot(np.append(square[0],square[0,0]),np.append(square[1],square[1,0]), color = 'red', label = 'original', marker = 'o')
plt.plot(np.append(rotsq[0],rotsq[0,0]),np.append(rotsq[1],rotsq[1,0]), color = 'blue', label = 'rotated', marker = 'o')
plt.plot(np.append(chainsq[0],chainsq[0,0]),np.append(chainsq[1],chainsq[1,0]), color = 'green', label = 'chained', marker = 'o')
plt.axhline(y=0, color = 'black', linestyle = '--')
plt.axvline(x=0, color = 'black', linestyle = '--')
plt.axis('equal')
plt.grid(True, linestyle = '-', alpha = 0.5)
plt.legend()
plt.show()

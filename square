import matplotlib.pyplot as plt
import numpy as np
def rot2d(theta):
    c,s = np.cos(theta), np.sin(theta)
    return np.array([[c,-s],[s,c]])
square = np.array([[0,1,1,0],[0,0,1,1]])
theta = np.pi/4
R =rot2d(theta)
rotatedsquare = R @ square
isto = np.allclose(R @ R.T, np.eye(2))
istdet = np.isclose(np.linalg.det(R), 1)
plt.figure(figsize=(8,8))
plt.plot(np.append(square[0],square[0,0]),np.append(square[1],square[1,0]), color='blue', label = 'og square', marker = 'o')
plt.plot(np.append(rotatedsquare[0],rotatedsquare[0,0]),np.append(rotatedsquare[1],rotatedsquare[1,0]), color='red', label = 'og square', marker = 'o')
plt.axhline(0, color='black', linestyle='-')
plt.axvline(0, color='black', linestyle='-')
plt.grid(True, linestyle='--')
plt.axis('equal')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
def hom2d(theta, tx, ty):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s, tx], [s, c, ty], [0, 0, 1]])
L1 = 1.0
L2 = 0.7
configs = [
    (0, 0, "Configuration 1: θ1=0°, θ2=0°\nExpected End: (1.7, 0)", 1),
    (90, 0, "Configuration 2: θ1=90°, θ2=0°\nExpected End: (0, 1.7)", 2),
    (0, 90, "Configuration 3: θ1=0°, θ2=90°\nExpected End: (1, 0.7)", 3)]
fig, axes = plt.subplots(1, 3, figsize=(20, 10))
for deg1, deg2, title, idx in configs:
    ax = axes[idx - 1]
    theta1 = np.radians(deg1)
    theta2 = np.radians(deg2)
    base = np.array([0,0])
    TL1 = hom2d(theta1, 0, 0) @ hom2d(0, L1, 0)
    TL2 = TL1 @ hom2d(theta2,0, 0) @ hom2d(0, L2, 0)
    elbow = TL1[:2, 2]
    end_effector = TL2[:2, 2]
    xcord = [base[0], elbow[0], end_effector[0]]
    ycord = [base[1], elbow[1], end_effector[1]]
    ax.plot(xcord, ycord, color="red", ls="--", lw=2, marker= 'o')
    ax.plot(end_effector[0], end_effector[1], 'ro', markersize=10, label='End Effector')
    ax.text(end_effector[0] + 0.1, end_effector[1] + 0.1, f"({end_effector[0]:.1f}, {end_effector[1]:.1f})", weight='bold')
    ax.axhline(y=0, color='k', linestyle='--')
    ax.axvline(x=0, color='k', linestyle='--')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, alpha=0.5)
    ax.set_title(title, fontsize=20)
plt.tight_layout()
plt.show()




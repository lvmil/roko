import matplotlib.pyplot as plt
import numpy as np
L1 = 1.0
L2 = 0.7
def fk2d(theta1, theta2):
    base = np.array([0.0,0.0])
    elbow = np.array(([L1 * np.cos(theta1), L1 * np.sin(theta1)]))
    ee = elbow + np.array([L2 * np.cos(theta1 + theta2), L2 * np.sin(theta1 + theta2)])
    return base, elbow, ee
def ik2d(x,y,elbow_up=True):
    r_sq = x ** 2 + y ** 2
    cos_theta2 = (r_sq - L1 ** 2 - L2 ** 2) / (2 * L1 * L2)
    if abs(cos_theta2) > 1.0:
        raise ValueError("Target coordinate is out of the arm's reach!")
    theta2 = -np.arccos(cos_theta2) if elbow_up else np.arccos(cos_theta2)
    theta1 = np.arctan2(y, x) - np.arctan2(L2 * np.sin(theta2), L1 + L2 * np.cos(theta2))
    return theta1, theta2
target_x, target_y = 1.2, 0.5
t1_up, t2_up = ik2d(target_x, target_y, elbow_up=True)
t1_down, t2_down = ik2d(target_x, target_y, elbow_up=False)
_, _, ee_up = fk2d(t1_up, t2_up)
_, _, ee_down = fk2d(t1_down, t2_down)
print(f"Target Input Location: ({target_x}, {target_y})")
print(f"Verification (Elbow Up)   -> FK Output: ({ee_up[0]:.4f}, {ee_up[1]:.4f}) | Match: {np.allclose(ee_up, [target_x, target_y])}")
print(f"Verification (Elbow Down) -> FK Output: ({ee_down[0]:.4f}, {ee_down[1]:.4f}) | Match: {np.allclose(ee_down, [target_x, target_y])}")
plt.figure(figsize=(8, 8))
b_up, el_up, _ = fk2d(t1_up, t2_up)
plt.plot([b_up[0], el_up[0], target_x], [b_up[1], el_up[1], target_y],
         color='blue', marker='o', lw=3, label='Elbow Up (Left-handed)')
b_down, el_down, _ = fk2d(t1_down, t2_down)
plt.plot([b_down[0], el_down[0], target_x], [b_down[1], el_down[1], target_y],
         color='orange', marker='o', lw=3, linestyle='--', label='Elbow Down (Right-handed)')
plt.plot(target_x, target_y, 'ro', markersize=10, zorder=5, label='Target')
plt.text(target_x + 0.05, target_y + 0.05, f"Target\n({target_x}, {target_y})", weight='bold', color='red')
plt.axhline(0, color='black', alpha=0.3, ls=':')
plt.axvline(0, color='black', alpha=0.3, ls=':')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True, alpha=0.3)
plt.title("2-Link Inverse Kinematics Solutions")
plt.legend()
plt.show()
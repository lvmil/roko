import matplotlib.animation as func_animation
import matplotlib.pyplot as plt
import numpy as np
L1 = 1.0
L2 = 0.7
def fk2d(theta1, theta2):
    base = np.array([0.0, 0.0])
    elbow = np.array([L1 * np.cos(theta1), L1 * np.sin(theta1)])
    ee = elbow + np.array([L2 * np.cos(theta1 + theta2), L2 * np.sin(theta1 + theta2)])
    return base, elbow, ee
def ik2d(x, y, elbow_up=True):
    r_sq = x ** 2 + y ** 2
    cos_theta2 = (r_sq - L1 ** 2 - L2 ** 2) / (2 * L1 * L2)
    cos_theta2 = np.clip(cos_theta2, -1.0, 1.0)
    theta2 = -np.arccos(cos_theta2) if elbow_up else np.arccos(cos_theta2)
    theta1 = np.arctan2(y, x) - np.arctan2(L2 * np.sin(theta2), L1 + L2 * np.cos(theta2))
    return theta1, theta2
fps = 120
angles = np.linspace(0, np.pi * 2, fps)
targetx = 0.6 + 0.4 * np.cos(angles)
targety = 0.6 + 0.4 * np.sin(angles)
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal', adjustable='box')
ax.grid(True, alpha=0.3)
ax.axhline(0, color='black', alpha=0.2, ls=':')
ax.axvline(0, color='black', alpha=0.2, ls=':')
ax.plot(targetx, targety, color='gray', linestyle='--', alpha=0.5, label='Target Path')
arm_line, = ax.plot([], [], color='blue', marker='o', lw=3, markersize=8, label='Robotic Arm')
target_dot, = ax.plot([], [], 'ro', markersize=10, label='Moving Target')
ax.set_title("Robot Arm Tracking a Circular Target Profile", fontsize=12)
ax.legend(loc='upper left')
def init():
    arm_line.set_data([], [])
    target_dot.set_data([], [])
    return arm_line, target_dot
def update(frame):
    x = targetx[frame]
    y = targety[frame]
    try:
        t1, t2 = ik2d(x, y, elbow_up=False)
        base, elbow, ee = fk2d(t1, t2)
        arm_line.set_data([base[0], elbow[0], ee[0]], [base[1], elbow[1], ee[1]])
        target_dot.set_data([x],[y])
    except ValueError:
     pass
    return arm_line, target_dot
ani = func_animation.FuncAnimation(fig, update, frames=fps, init_func=init, interval=25, blit=True)
plt.show()


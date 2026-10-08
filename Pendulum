import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation
g = 9.81
L = 2
initials = [np.pi/4,0]
ts, tend = 0, 10
fps = 30
frames = int(tend-ts) * fps
t_eval = np.linspace(ts, tend, frames)
def pend(t, state, g, L ):
    theta, omega = state
    dthetadt = omega
    domegadt = -(g / L) * np.sin(theta)
    return [dthetadt, domegadt]
sol = solve_ivp(pend, [ts, tend], initials, args=[g, L], t_eval=t_eval)
thist = sol.y[0]
xcord = L * np.sin(thist)
ycord = -L * np.cos(thist)
fig, ax = plt.subplots(figsize=(8,8))
ax.set_xlim(-L - 0.5, L + 0.5)
ax.set_ylim(-L - 0.5, 0.5)
ax.set_aspect('equal')
ax.grid(True)
ax.set_title('pendulum')
line, = ax.plot([], [], 'o-', lw= 3, ms= 10, color='blue', markerfacecolor='red')
trail, = ax.plot([], [], '-', color='red', alpha=0.2)
def init():
    line.set_data([], [])
    trail.set_data([], [])
    return line, trail
def update(frame):
    line.set_data([0,xcord[frame]],[0,ycord[frame]])
    trailst = max(0, frame - 10)
    trail.set_data(xcord[trailst:frame],ycord[trailst:frame])
    return line, trail
ani = FuncAnimation(fig, update, frames=frames, init_func=init, interval=1000/fps, blit=True)
plt.show()

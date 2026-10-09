import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
m = 1
c = 0.5
k = 8
initials = [2,0]
ts, tend = 0, 10
dt = 0.05
teuler = np.arange(ts, tend + dt, dt)
xeuler = np.zeros(len(teuler))
veuler = np.zeros(len(teuler))
xeuler[0] = initials[0]
veuler[0] = initials[1]
for i in range(len(teuler)-1):
    dxdt = veuler[i]
    dvdt = -(c/m) * veuler[i] - (k/m) * xeuler[i]
    xeuler[i + 1] = xeuler[i] + dt * dxdt
    veuler[i+1] = veuler[i] + dt * dvdt

def osys(t, state, m, c, k):
    x, v = state
    dxdt = v
    dvdt = -(c/m) * v - (k/m) * x
    return [dxdt, dvdt]
sol = solve_ivp(osys, [ts,tend], initials, args=(m,c,k),t_eval=teuler)
plt.figure(figsize=(10, 5))
plt.plot(teuler, xeuler, 'o--', label='Hand-coded Euler Method', alpha=0.7)
plt.plot(sol.t, sol.y[0], '-', label='SciPy solve_ivp (RK45)', linewidth=2)
plt.title('Mass-Spring-Damper System Response')
plt.xlabel('Time (seconds)')
plt.ylabel('Displacement x(m)')
plt.grid(True)
plt.legend()
plt.show()

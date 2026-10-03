import numpy as np
import time
np.random.seed(42)
vectors = np.random.rand(1000, 3)
print('Benchmark for Coding Efficiency')
startloop = time.perf_counter()
norms = []
for v in vectors:
    value = np.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    norms.append(value)
endloop = time.perf_counter()
delta = endloop - startloop


startloopnp = time.perf_counter()
valuenp = np.linalg.norm(vectors, axis=1)
endloopnp = time.perf_counter()
deltanp = endloopnp - startloopnp
print(f'Loop speed for normal method is {delta:.5f}s')
print(f'Loop speed for np method is {deltanp:.5f}s')
speedup = delta / deltanp
print(f'np is roughly {speedup:.2f}x faster')
assert np.allclose(norms, valuenp)

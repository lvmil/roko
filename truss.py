import numpy as np
cos = 4/5
sin = 3/5
A = np.array([[0,cos,1,0,1,0,0,0],[0,sin,0,0,0,1,0,0],[1,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,1],[-1,-cos,0,0,0,0,0,0],[0,-sin,0,-1,0,0,0,0],[0,0,-1,0,0,0,0,0],[0,0,0,1,0,0,0,0]])
B = np.array([0,0,0,0,0,0,0,10])
try:
    forces = np.linalg.solve(A,B)
    labels = ["S2 (Top Chord)", "S3 (Diagonal)", "S4 (Bottom Chord)", "S5 (End Vertical)",
              "R1x", "R1y", "R2x", "R2y"]
    print("--- Truss Equilibrium Results ---")
    for label, force in zip(labels, forces):
        # Positive values = Tension, Negative values = Compression
        print(f"{label:18} : {force:6.2f} kN")

except np.linalg.LinAlgError:
    print("The system matrix is singular. Check your boundary conditions or truss stability.")

import matplotlib.pyplot as plt
import numpy as np

shift_points_y = np.array([49, -22, 28, -65, 12, -66, 20, -80, 8, 0])
shift_points_x = np.array(["x5", "y1", "x4", "y2", "x3", "y3", "x2", "y4", "x1", "y5"])
plt.plot(shift_points_x, shift_points_y, color="g", marker="o")
plt.axhline(y=0, xmin=0.0, xmax=1.0)

plt.xlabel('Permutation')
plt.ylabel('Distance to zero')
plt.show()

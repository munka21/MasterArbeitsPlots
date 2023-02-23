import matplotlib.pyplot as plt
import numpy as np


shift_points_y = np.array([134, 149, 179, 221])
shift_points_x = np.array([1, 2, 3, 4])
plt.plot(shift_points_x, shift_points_y, color="g", marker=".")

shift_points_y = np.array([102, 103, 105, 113])
shift_points_x = np.array([1, 2, 3, 4])
plt.plot(shift_points_x, shift_points_y, color="r", marker=".")

plt.legend(['p_Algo', 'OPT'])

plt.yticks(np.arange(0, 241, 20.0))
plt.xticks(np.arange(1, 5, 1.0))

plt.axhline(y=0, xmin=0.0, xmax=1.0)
plt.ylabel('Target Function')
plt.show()

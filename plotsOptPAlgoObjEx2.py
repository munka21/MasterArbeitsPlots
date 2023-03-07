import matplotlib.pyplot as plt
import numpy as np


shift_points_y = np.array([271, 298, 316, 409])
shift_points_x = np.array([1, 2, 3, 4])
plt.plot(shift_points_x, shift_points_y, color="g", marker=".")

shift_points_y = np.array([202, 204, 207, 211])
shift_points_x = np.array([1, 2, 3, 4])
plt.plot(shift_points_x, shift_points_y, color="r", marker=".")

plt.legend(['p_Algo', 'OPT'])

plt.yticks(np.arange(100, 426, 25.0))
plt.xticks(np.arange(1, 5, 1.0))

plt.ylabel('Target Function')
plt.show()
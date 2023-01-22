import matplotlib.pyplot as plt
import numpy as np

rounding_points_x = np.array([10, 20, 50, 100, 200])
rounding_points_y = np.array([0.1, 0.5, 2.5, 16.2, 163.1])
plt.plot(rounding_points_x, rounding_points_y)

shift_points_x = np.array([10, 20, 50, 100, 200])
shift_points_y = np.array([0.04, 0.2, 2.9, 49.6, 787.5])
plt.plot(shift_points_x, shift_points_y)

plt.xlabel('Number of jobs')
plt.ylabel('Time in ms')
plt.legend(['Rounding', 'Shift'])
plt.show()
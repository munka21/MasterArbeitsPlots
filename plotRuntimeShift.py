import matplotlib.pyplot as plt
import numpy as np

shift_points_x = np.array([10, 20, 50, 100, 200])
shift_points_y = np.array([0.04, 0.2, 2.9, 49.6, 787.5])
plt.plot(shift_points_x, shift_points_y)

plt.xlabel('Number of jobs')
plt.ylabel('Time in ms')
plt.legend(['Shift'])
plt.show()
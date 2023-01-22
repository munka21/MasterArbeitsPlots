import matplotlib.pyplot as plt
import numpy as np

algo_points_x = np.array([10, 20, 50, 100, 200])
algo_points_y = np.array([3.5, 8.5, 82, 824.6, 6567.8])
plt.plot(algo_points_x, algo_points_y)

rounding_points_x = np.array([10, 20, 50, 100, 200])
rounding_points_y = np.array([0.1, 0.5, 2.5, 16.2, 163.2])
plt.plot(rounding_points_x, rounding_points_y)

shift_points_x = np.array([10, 20, 50, 100, 200])
shift_points_y = np.array([0.04, 0.2, 2.9, 49.6, 787.5])
plt.plot(shift_points_x, shift_points_y)

lp_points_x = np.array([10, 20, 50, 100, 200])
lp_points_y = np.array([3.3, 7.9, 76.6, 758.9, 5617.3])
plt.plot(lp_points_x, lp_points_y)

plt.xlabel('Number of jobs')
plt.ylabel('Time in ms')
plt.legend(['Time of Algo', 'Rounding', 'Shift', 'LP'])
plt.show()
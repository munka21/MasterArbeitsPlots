import matplotlib.pyplot as plt
import numpy as np

algo_points_x = np.array([10, 20, 50, 100])
algo_points_y = np.array([3.5, 8.5, 82, 824.6])
plt.plot(algo_points_x, algo_points_y)

rounding_points_x = np.array([10, 20, 50, 100])
rounding_points_y = np.array([0.1, 0.5, 2.5, 16.2])
plt.plot(rounding_points_x, rounding_points_y)

shift_points_x = np.array([10, 20, 50, 100])
shift_points_y = np.array([0.04, 0.2, 2.9, 49.6])
plt.plot(shift_points_x, shift_points_y)

lp_points_x = np.array([10, 20, 50, 100])
lp_points_y = np.array([3.3, 7.9, 76.6, 758.9])
plt.plot(lp_points_x, lp_points_y)

plt.xticks(np.arange(10, 101, 10))

plt.xlabel('Number of elements in sets')
plt.ylabel('Time in ms')
plt.legend(['Complete algorithm', 'Rounding', 'Shift', 'LP'])
plt.show()
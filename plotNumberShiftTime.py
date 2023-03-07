
import matplotlib.pyplot as plt
import numpy as np
Int = {10, 20, 50, 100, 200}
algo_points_y = np.array([25, 110, 616, 2114, 6824])
algo_points_x = np.array([10, 20, 50, 100, 200])
plt.subplot(1, 2, 1)
plt.plot(algo_points_x, algo_points_y,  marker=".")

plt.xlabel('Size of Instance')
plt.ylabel('Number of shifts')
plt.xticks(algo_points_x)

algo_points_y = np.array([0.04, 0.14, 2.98, 49.58, 787.46])
algo_points_x = np.array([10, 20, 50, 100, 200])
plt.subplot(1, 2, 2)
plt.plot(algo_points_x, algo_points_y,  marker=".")

plt.xlabel('Size of Instance')
plt.ylabel('Time per shift in ms')
plt.xticks(algo_points_x)

plt.show()

import matplotlib.pyplot as plt
import numpy as np

algo_points_x = np.array([10, 20, 50, 100])
algo_points_y = np.array([3.5, 8.5, 82, 824])
plt.plot(algo_points_x, algo_points_y)

rounding_points_x = np.array([10, 20, 50, 100])
rounding_points_y = np.array([59.17, 1235.47, 79859.04, 16835609.43])
plt.plot(rounding_points_x, rounding_points_y)

plt.yticks(np.arange(0, 17000001, 1000000))
plt.xticks(np.arange(10, 101, 10))

plt.xlabel('Number of elements in sets')
plt.ylabel('Time in ms')
plt.legend(['Algorithm', 'Optimal solution'])




algo_points_x = np.array([10, 20, 50])
algo_points_y = np.array([3.5, 8.5, 82])
plt.plot(algo_points_x, algo_points_y)

rounding_points_x = np.array([10, 20, 50])
rounding_points_y = np.array([59.17, 1235.47, 79859.04])
plt.plot(rounding_points_x, rounding_points_y)

plt.yticks(np.arange(0, 80001, 10000))
plt.xticks(np.arange(10, 51, 10))

plt.xlabel('Number of elements in sets')
plt.ylabel('Time in ms')
plt.legend(['Algorithm', 'Optimal solution'])


plt.show()

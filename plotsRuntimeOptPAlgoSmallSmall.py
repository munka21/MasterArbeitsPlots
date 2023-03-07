import matplotlib.pyplot as plt
import numpy as np

#plot 1:
algo_points_x = np.array([10, 20, 50, 100])
algo_points_y = np.array([3.5, 8.5, 82, 824])

plt.subplot(1, 2, 2)
plt.plot(algo_points_x, algo_points_y)

rounding_points_x = np.array([10, 20, 50, 100])
rounding_points_y = np.array([59.17, 1235.47, 79859.04, 16835609.43])

plt.subplot(1, 2, 2)
plt.plot(rounding_points_x, rounding_points_y)
plt.yticks(np.arange(0, 17000001, 1000000))
plt.xticks(np.arange(10, 101, 10))

plt.xlabel('Number of elements in sets')
plt.ylabel('Time in ms')
plt.legend(['Algorithm', 'Optimal solution'])

#plot 2:
algo_points_x = np.array([10, 20, 50])
algo_points_y = np.array([3.5, 8.5, 82])

plt.subplot(1, 2, 1)
plt.plot(algo_points_x,algo_points_y)

rounding_points_x = np.array([10, 20, 50])
rounding_points_y = np.array([59.17, 1235.47, 79859.04])

plt.subplot(1, 2, 1)
plt.plot(rounding_points_x, rounding_points_y)
plt.yticks(np.arange(0, 80001, 10000))
plt.xticks(np.arange(10, 51, 10))

plt.xlabel('Number of elements in sets')
plt.ylabel('Time in ms')
plt.legend(['Algorithm', 'Optimal solution'])

plt.show()
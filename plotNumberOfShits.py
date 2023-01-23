import matplotlib.pyplot as plt
import numpy as np

shift_points_x = np.array([10, 20, 50, 100, 200])
shift_points_y = np.array([25, 110, 616, 2114, 6824])
plt.plot(shift_points_x, shift_points_y)

plt.xlabel('Number of jobs')
plt.ylabel('Average Number of Shifts in Matrix')
plt.show()
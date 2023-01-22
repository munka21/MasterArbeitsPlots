import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
plt.plot(xpoints, ypoints)

mpoints = np.array([2, 3, 5, 9])
npoints = np.array([2, 7, 1, 12])

plt.plot(mpoints, npoints)

plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.legend(['element 1', 'element 2'])
plt.show()
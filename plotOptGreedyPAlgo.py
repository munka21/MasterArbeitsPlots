import matplotlib.pyplot as plt
import numpy as np


'''
Number of jobs: 10
Max sum of jobs: 700
Max size of one job: 100

Y:[50, 56, 35, 100, 42, 100, 85, 70, 99, 63]
X:[100, 100, 97, 95, 77, 61, 45, 43, 41, 41]

$Permutation = \{41, 50, 95, 56, 61, 35, 45, 100, 77, 42, 97, 100, 100, 85, 100, 70, 43, 99, 41, 63\} = \{x_{10}, y_{1}, x_{4}, y_{2}, x_{6}, y_{3}, x_{7}, y_{4}, x_{5}, y_{5}, x_{3}, y_{6}, x_{1}, y_{7}, x_{2}, y_{8}, x_{8}, y_{9}, x_{9}, y_{10}\}$. 

pAlgo Solution: [41, 50, 95, 56, 61, 35, 45, 100, 77, 42, 97, 100, 100, 85, 100, 70, 43, 99, 41, 63]
Tank Log End:: 
[41, -9, 86, 30, 91, 56, 101, 1, 78, 36, 133, 33, 133, 48, 148, 78, 121, 22, 63, 0]
Min Value:-9 Max Value:148 Ziel:157
Greedy Solution: [41, 50, 41, 56, 43, 35, 45, 100, 77, 42, 61, 100, 95, 85, 97, 70, 100, 99, 100, 63]
Tank Log End:: 
[41, -9, 32, -24, 19, -16, 29, -71, 6, -36, 25, -75, 20, -65, 32, -38, 62, -37, 63, 0]
Min Value:-75 Max Value:63 Ziel:138
OPT Solution: [43, 50, 45, 56, 41, 35, 77, 100, 100, 42, 41, 100, 95, 85, 61, 70, 100, 99, 97, 63]
Tank Log End:: 
[43, -7, 38, -18, 23, -12, 65, -35, 65, 23, 64, -36, 59, -26, 35, -35, 65, -34, 63, 0]
Min Value:-36 Max Value:65 Ziel:101

'''

#permutation p_Algo: [41, 50, 95, 56, 61, 35, 45, 100, 77, 42, 97, 100, 100, 85, 100, 70, 43, 99, 41, 63]
shift_points_y = np.array([41, -9, 86, 30, 91, 56, 101, 1, 78, 36, 133, 33, 133, 48, 148, 78, 121, 22, 63, 0])
shift_points_x = np.array(["x1", "y1", "x2", "y2", "x3", "y3", "x4", "y4", "x5", "y5","x6", "y6", "x7", "y7", "x8", "y8", "x9", "y9", "x10", "y10"])
plt.plot(shift_points_x, shift_points_y, color="g", marker=".")
'''
#permutation Greedy: [41, 50, 41, 56, 43, 35, 45, 100, 77, 42, 61, 100, 95, 85, 97, 70, 100, 99, 100, 63]
shift_points_y = np.array([41, -9, 32, -24, 19, -16, 29, -71, 6, -36, 25, -75, 20, -65, 32, -38, 62, -37, 63, 0])
shift_points_x = np.array(["x1", "y1", "x2", "y2", "x3", "y3", "x4", "y4", "x5", "y5","x6", "y6", "x7", "y7", "x8", "y8", "x9", "y9", "x10", "y10"])
plt.plot(shift_points_x, shift_points_y, color="y", marker=".")
'''
#permutation OPT: [43, 50, 45, 56, 41, 35, 77, 100, 100, 42, 41, 100, 95, 85, 61, 70, 100, 99, 97, 63]
shift_points_y = np.array([43, -7, 38, -18, 23, -12, 65, -35, 65, 23, 64, -36, 59, -26, 35, -35, 65, -34, 63, 0])
shift_points_x = np.array(["x1", "y1", "x2", "y2", "x3", "y3", "x4", "y4", "x5", "y5","x6", "y6", "x7", "y7", "x8", "y8", "x9", "y9", "x10", "y10"])
plt.plot(shift_points_x, shift_points_y, color="r", marker=".")

plt.legend(['p_Algo','OPT'])

plt.yticks(np.arange(-75, 151, 15.0))

plt.axhline(y=0, xmin=0.0, xmax=1.0)
plt.xlabel('Permutation')
plt.ylabel('Distance to zero')
plt.grid(axis = 'y')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

y = np.array([ 758.9, 49.6, 16.2])
mylabels = ['LP', 'Shift', 'Rounding']
myexplode = [0.3, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, startangle = 70)
plt.show()
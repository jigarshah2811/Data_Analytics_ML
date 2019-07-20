import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import warnings

np.set_printoptions(precision=3, suppress=True)
warnings.filterwarnings('ignore')

data = np.genfromtxt('../resources/baseball/Batting.csv', skip_header=1,
                     usecols=(1, 6, 8), delimiter=',', dtype=float)

data = data[data[:, 1] >= 502]
data = data[data[:, 0] >= 1957]

avgs = data[:, 2] / data[:, 1]
data = np.column_stack([data, avgs])

data = data[data[:, 3].argsort()]


fig = plt.figure(figsize=(8, 6))
ax = axes3d.Axes3D(fig)
x, y, z = data[-1:-100:-1, 3], data[-1:-100:-1, 2], data[-1:-100:-1, 0]
ax.scatter(x, y, z)
ax.set_xlabel('Averages')
ax.set_ylabel('At Bats')
ax.set_zlabel('Year')
plt.show()
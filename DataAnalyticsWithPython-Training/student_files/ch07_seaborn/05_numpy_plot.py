'''
    05_numpy_plot.py

    Plotting numpy data and using Matplotlib APIs to assist in rendering.

'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('classic')

rand_state = np.random.RandomState(0)
x = np.linspace(0, 10, 100)
y = np.cumsum(rand_state.randn(100, 3), 0)

plt.plot(x, y)
plt.legend(['First', 'Second', 'Third'], ncol=1, loc='best')
plt.show()


# now accomplished using Seaborn styles
import seaborn as sns
sns.set()

plt.plot(x, y)
plt.legend(['First', 'Second', 'Third'], ncol=1, loc='best')
plt.show()
'''
    04_stripplot.py

    Plotting a stripplot() and swarmplot of car crashes data.

'''
import matplotlib.pyplot as plt
import seaborn as sns

crashes = sns.load_dataset('car_crashes')
sns.stripplot(y='total', data=crashes)
plt.xlabel('total')
plt.ylabel('values')
plt.show()
sns.stripplot(y='total', data=crashes, jitter=0.02)
plt.xlabel('total')
plt.ylabel('values')
plt.show()
sns.swarmplot(y='total', data=crashes)
plt.xlabel('total')
plt.ylabel('values')
plt.show()

sns.boxplot(y='total', data=crashes)
sns.stripplot(y='total', data=crashes, jitter=0.02)
plt.xlabel('total')
plt.ylabel('values')
plt.show()

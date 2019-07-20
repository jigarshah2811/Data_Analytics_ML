'''
    07_countplot.py

'''
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
titanic = sns.load_dataset('titanic')

sns.countplot(x='sex', data=titanic)
plt.show()

sns.set(palette='Blues_d')
sns.countplot(x='parch', data=titanic, hue='class')
plt.legend(loc='upper right')
plt.show()
'''
    08_boxplot.py

'''
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()
titanic = sns.load_dataset('titanic')
titanic.dropna(subset=['age'], inplace=True)
sns.distplot(titanic.age)
sns.kdeplot(titanic.age, shade=True)
plt.show()

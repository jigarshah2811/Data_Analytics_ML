'''
    03_pairplot.py

    A pairplot can plot multiple features against your response

'''
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
crashes = sns.load_dataset('car_crashes')

sns.pairplot(crashes, x_vars=['not_distracted', 'alcohol', 'speeding'], y_vars='total')
plt.show()

sns.pairplot(crashes, x_vars=['not_distracted', 'alcohol', 'speeding'], y_vars='total',
             aspect=0.75, size=7.5)
plt.show()

sns.pairplot(crashes, x_vars=['not_distracted', 'alcohol', 'speeding'], y_vars='total',
             aspect=0.75, size=7.5, kind='reg')
plt.show()
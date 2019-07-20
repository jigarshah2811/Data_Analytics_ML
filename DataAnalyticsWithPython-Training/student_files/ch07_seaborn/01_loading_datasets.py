'''
    01_loading_datasets.py

    This example shows how to load an external dataset from a
    predefined GitHub repository.

'''

import matplotlib.pyplot as plt
import seaborn as sns

crashes = sns.load_dataset('car_crashes')
print(crashes.head())
print(crashes.shape)
most = crashes.sort_values(by='total', ascending=False).head(10)
sns.barplot(x='total', y='abbrev', data=most)
plt.show()
sns.set()
sns.barplot(x='total', y='abbrev', data=most)
plt.show()
sns.barplot(x='total', y='abbrev', data=most, palette='Reds_d')
plt.show()
sns.barplot(x='total', y='abbrev', data=most, palette='Blues_d')
plt.show()
sns.barplot(x='total', y='abbrev', data=most, palette='deep')
plt.show()



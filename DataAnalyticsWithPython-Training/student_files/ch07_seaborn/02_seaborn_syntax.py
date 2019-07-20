'''
    02_seaborn_syntax.py

    Shows how to create Seaborn plots using the Seaborn functions (lmplot in
    this example).

'''
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
crashes = sns.load_dataset('car_crashes')

sns.lmplot(x='alcohol', y='total', data=crashes)
plt.show()

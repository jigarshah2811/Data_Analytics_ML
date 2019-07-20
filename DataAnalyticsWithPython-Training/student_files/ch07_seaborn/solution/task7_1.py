import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()
batting = pd.read_csv('../../resources/baseball/Batting.csv',
                      usecols=(1, 6, 8), skiprows=1,
                      names=['year', 'atbats', 'hits'])

batting = batting.loc[batting['atbats'] >= 502]
batting = batting.loc[batting['year'] >= 2000]
batting['averages'] = batting['hits'] / batting['atbats']

sns.pairplot(batting, x_vars=['year', 'atbats', 'hits'], y_vars='averages',
             hue='year', aspect=0.7, size=7.5)
plt.show()

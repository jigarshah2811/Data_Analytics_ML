import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()
batting = pd.read_csv('../resources/baseball/Batting.csv',
                      usecols=(1, 6, 8), skiprows=1,
                      names=['year', 'atbats', 'hits'])

batting = batting.loc[batting['atbats'] >= 502]
batting = batting.loc[batting['year'] >= 2000]
batting['averages'] = batting['hits'] / batting['atbats']

# create and display a pairplot() using averages as the response and the remaining columns
# as features.  Plot each feature (using x_vars) vs. the response

# show your results
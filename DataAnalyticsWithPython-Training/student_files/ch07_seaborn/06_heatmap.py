'''
    06_heatmap.py

    Plotting a heatmap of 3 columns from the car crashes dataset.

'''
import matplotlib.pyplot as plt
import seaborn as sns

crashes = sns.load_dataset('car_crashes')
most = crashes.sort_values(by='total', ascending=False).head(10)

print(most[['speeding', 'alcohol', 'not_distracted']])
sns.heatmap(most[['speeding', 'alcohol', 'not_distracted']])
plt.show()

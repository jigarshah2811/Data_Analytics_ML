import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model

df = pd.read_csv('../resources/baseball/Batting.csv', usecols=(6, 8))
df.columns = ['atbats', 'hits']
df['avgs'] = df['hits'] / df['atbats']
df2 = df.loc[(df['atbats'] >= 502)]

regr = linear_model.LinearRegression()
x = df2['avgs'].values[:, None]             # must use form: [[x1], [x2], [x3], ...]
y = df2['atbats'].values[:, None]           # must use form: [[y1], [y2], [y3], ...]

regr.fit(x, y)

print('Coefficients: ', regr.coef_)
print('Intercept: ', regr.intercept_)
print('Variance: ', regr.score(x, y))

plt.scatter(df2['avgs'], df2['atbats'], color='#24a1f2', marker='.')
plt.plot(x, regr.predict(x))
plt.xlim(0.2, 0.45)
plt.show()


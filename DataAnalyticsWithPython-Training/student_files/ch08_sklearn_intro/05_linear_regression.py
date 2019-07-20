import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


np.set_printoptions(suppress=True, precision=1)
sns.set()
crashes = sns.load_dataset('car_crashes')
print(crashes.head())
sns.lmplot(x='alcohol', y='total', data=crashes)
plt.show()


X = crashes['alcohol']
y = crashes['total']

# splits 75-25 train-test by default
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

lm = LinearRegression()
lm.fit(X_train[:, None], y_train)

y_pred = lm.predict(X=X_test[:, None])

print(y_pred)
print(y_test.values)
print(np.sqrt(mean_squared_error(y_test.values, y_pred)))

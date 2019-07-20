import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

points = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
data_array = np.array(points)
X = data_array[:, 0]
X_reshaped = X[:, None]
print(X)
print(X_reshaped)
y = data_array[:, 1]
plt.plot(X, y, 'go')
plt.xlim(0, 6)
plt.ylim(0, 6)

lm = LinearRegression()
lm.fit(X_reshaped, y)
x_test = np.linspace(0, 6, 37)[:, None]
y_test = lm.predict(x_test)
plt.plot(x_test, y_test, 'r-')
plt.show()
print('Coefficients: ', lm.coef_)
print('Intercept: ', lm.intercept_)
print('R-Squared: ', lm.score(x_test, y_test-1))


points = [(1, 1), (2, 3), (3, 1), (3, 5), (4, 6)]
data_array = np.array(points)
X = data_array[:, 0]
X_reshaped = X[:, None]
print(X)
print(X_reshaped)
y = data_array[:, 1]
plt.plot(X, y, 'go')
plt.xlim(0, 5)
plt.ylim(0, 7)

lm = LinearRegression()
lm.fit(X_reshaped, y)
x_test = np.linspace(0, 5, 31)[:, None]
y_test = lm.predict(x_test)
# plt.plot(x_test, y_test, 'r-')
plt.show()

print('Coefficients: ', lm.coef_)
print('Intercept: ', lm.intercept_)
print('R-Squared: ', lm.score(x_test, y_test-1))

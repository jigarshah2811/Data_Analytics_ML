import pandas as pd
import sklearn.metrics as mean_squared_error
from sklearn.linear_model import LinearRegression

filename = '../resources/Batting.csv'
data = pd.read_csv(filename, usecols=(1,2,4,12))
print("Data Shape: ", data.shape)



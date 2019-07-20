import numpy as np
import pandas as pd

data1 = np.arange(1, 10).reshape(3, 3)
df1 = pd.DataFrame(data1, columns=['a', 'b', 'c'])
print(df1)

data2 = np.arange(1, 13).reshape(4, 3)
df2 = pd.DataFrame(data2, columns=['d', 'b', 'e'])
print(df2)

merged1 = pd.merge(df1, df2, on='b')
print(merged1)

merged2 = pd.merge(df1, df2, left_on='a', right_on='d', how='outer')
print(merged2)

merged3 = pd.merge(df1, df2, left_on='a', right_on='d')
print(merged3)

merged4 = pd.merge(df1, df2, left_index=True, right_index=True)
print(merged4)

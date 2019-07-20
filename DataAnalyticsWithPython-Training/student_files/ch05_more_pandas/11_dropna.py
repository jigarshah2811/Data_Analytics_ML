"""

        11_dropna.py

        Use dropna() to remove columns containing NaN values.

"""
import numpy as np
import pandas as pd

sat_temps = pd.DataFrame(data=[(78, 50), (82, 52), (83, 53)],
                         index=['Colorado Springs', 'Canon City', 'Pueblo'],
                         columns=['High', 'Low'])
sat_humidity = pd.DataFrame([22, 18, 19, 25],
                            index=['Colorado Springs', 'Canon City', 'Pueblo', 'Denver'],
                            columns=['Humidity'])
temps_df = pd.concat([sat_temps, sat_humidity], axis=1)

temps_df.loc[(temps_df['High'] > 80), 'High'] = np.inf


print(temps_df)

temps_df.replace([np.inf, -np.inf], np.nan, inplace=True)
temps_df.dropna(subset=['Low'], inplace=True)

print(temps_df)

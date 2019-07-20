"""

        03_imputing.py

        Use fillna() to impute missing values.
        Use drop() to remove columns.
        Each of these is shown below...

"""
import pandas as pd

sat_temps = pd.DataFrame(data=[(78, 50), (82, 52), (83, 53)],
                         index=['Colorado Springs', 'Canon City', 'Pueblo'],
                         columns=['High', 'Low'])
sat_humidity = pd.DataFrame([22, 18, 19, 25],
                            index=['Colorado Springs', 'Canon City', 'Pueblo', 'Denver'],
                            columns=['% Hum'])
temps_df = pd.concat([sat_temps, sat_humidity], axis=1)
print(temps_df)


# ------------------------------
#   Imputing values...
temps_df['High'].fillna(value=80, inplace=True)
temps_df['Low'].fillna(52, inplace=True)
print(temps_df)


# ------------------------------
#   Copying a DataFrame...
temps_df2 = temps_df.copy(deep=True)
temps_df3 = temps_df.copy()                 # deep=True is the default


# ---------------------------------
#   Removing one or more columns...
temps_df2.drop(['Low', '% Hum'], axis=1, inplace=True)
print(temps_df2)

temps_df3.drop(temps_df3.columns[[1, 2]], axis=1, inplace=True)
print(temps_df3)

'''
    07_read_json.py     -   Shows the different values that orient=
                            accepts and the associated data format for
                            each one.
'''

import numpy as np
import pandas as pd

# -------------------------------------------------------------
# orient='records'
data = '''
    [
        {"name": "Fang", "type": "Dog", "age": 3},
        {"name": "Aragog", "type": "Spider", "age": 1},
        {"name": "Hedwig", "type": "Owl", "age": 2}
    ]
'''

df = pd.read_json(data, orient='records')
print(df)

# -------------------------------------------------------------
# orient='split'
data = '''
    {
        "columns": ["name", "type", "age"],
        "data": [["Aragog", "Spider", 1], ["Fang", "Dog", 3], ["Hedwig", "Owl", 2]],
        "index": [0, 1, 2]
    }
'''

df = pd.read_json(data, orient='split')
print(df)


# -------------------------------------------------------------
# orient='index'
data = '''
    {
        "0":{"name": "Hedwig", "type": "Owl", "age": 2},
        "1":{"name": "Fang", "type": "Dog", "age": 3},
        "2":{"name": "Aragog", "type": "Spider", "age": 1},
    }
'''

df = pd.read_json(data, orient='index')
print(df)


# -------------------------------------------------------------
# orient='columns'
data = '''
    {
        "name":{"0": "Aragog", "1": "Hedwig", "2": "Fang"},
        "type":{"0": "Spider", "1": "Owl", "2": "Dog"},
        "age":{"0": 1, "1": 2, "2": 3},
    }
'''

df = pd.read_json(data, orient='columns')
print(df)


# -------------------------------------------------------------
# orient='values'
data = '''
    [
        ["Aragog", "Spider", 1],
        ["Hedwig", "Owl", 2],
        ["Fang", "Dog", 3]
    ]
'''

df = pd.read_json(data, orient='values')
df.columns = ["name", "type", "age"]
print(df)

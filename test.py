import pandas as pd
import os
import random
import json

DATA_BASE_NAME = 'dataBase.csv'
data = {'key_pressed': [None],
         'mine_field': [None],
         'grass': [None],
         'soliderPosition': [None]}

"""raw = {'first_name': ['Sheldon', 'Raj', 'Leonard', 'Howard', 'Amy'],
                'last_name': ['Copper', 'Koothrappali', 'Hofstadter', 'Wolowitz', 'Fowler'],
                'age': [42, 38, 36, 41, 35],
                'Comedy_Score': [9, 7, 8, 8, 5],
                'Rating_Score': [25, 25, 49, 62, 70]}


df = pd.DataFrame(raw, columns=['first_name', 'last_name', 'age',
                                         'Comedy_Score', 'Rating_Score'])
df.to_csv('raw.csv', index=False)
print(df)"""
def init_data_base():
    if not os.path.exists(DATA_BASE_NAME):
        df = pd.DataFrame(data, columns=['key_pressed', 'mine_field', 'grass',
                                        'soliderPosition'])
        df.to_csv('database.csv', index=False)

init_data_base()




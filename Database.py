import pandas
import os

DATA_BASE_NAME = 'dataBase.csv'
DATA_FRAME = None


def init_data_base():
    if not os.path.exists(DATA_BASE_NAME):
        new_file = open(DATA_BASE_NAME, 'w')
        new_file.close()


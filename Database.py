import pandas
import os
import json
import consts
import Soldier
import MineField
import pygame
from csv import DictWriter

DATA_BASE_NAME = 'dataBase.csv'
data = {'key_pressed': [None],
        'mine_field': [None],
        'grass': [None],
        'soliderPosition': [None]
        }
field_names = ['key_pressed', 'mine_field', 'grass',
               'soliderPosition']


def init_data_base():
    if not os.path.exists(DATA_BASE_NAME):
        df = pandas.DataFrame(data,
                              columns=['key_pressed', 'mine_field', 'grass',
                                       'soliderPosition'])
        df.to_csv('database.csv', mode='w', header=True, index=False)


def convert_data_lists_to_srt(game_data):
    for key in game_data.keys():
        if type(game_data[key]) is list:
            game_data[key] = json.dumps(game_data[key])
    return game_data


def save_game(game_data):
    # game_data_bs = convert_data_lists_to_srt(game_data)
    # print(game_data_bs)

    # זה מכניס אבל נראה מוזר בהדפסה
    # df = pandas.DataFrame(game_data)
    # df2.to_csv('database.csv', mode='a', header=False, index=False)

    """df.loc[len(df.index)] = ['Amy', '89', "93", "h"]
    print(df)"""

    with open('database.csv', 'a') as f_object:
        # Pass the file object and a list
        # of column names to DictWriter()
        # You will get a object of DictWriter
        dictwriter_object = DictWriter(f_object, fieldnames=field_names)

        # Pass the dictionary as an argument to the Writerow()
        dictwriter_object.writerow(game_data)

        # Close the file object
        f_object.close()
        print()



"""def save_game(game_data, num_button_pressed):
    game_data = convert_data_lists_to_srt(game_data)
    # df = pandas.read_csv(DATA_BASE_NAME)
    # df.drop(index= df[df['key'] == num_button_pressed].index, inplace=True)
    # df.to_csv(DATA_BASE_NAME)
    new_data_frame = pandas.DataFrame([game_data])#, index=[num_button_pressed])
    new_data_frame.to_csv(DATA_BASE_NAME, mode='a', header=False)"""

"""def save_game(game_data):
    game_data = convert_data_lists_to_srt(game_data)
    new_data_frame = pandas.DataFrame([game_data])
    df = pandas.read_csv(DATA_BASE_NAME)
    if (df['num_button_pressed'] == game_data['num_button_pressed']).any():
        df.drop(index=df[df['num_button_pressed'] == game_data['num_button_pressed']].index, inplace=True)
        df.to_csv(DATA_BASE_NAME, mode='w', header=False)
    new_data_frame.to_csv(DATA_BASE_NAME, mode='a', header=False)"""

init_data_base()

save_game({'key_pressed': 4, 'mine_field': [[1, 1], [1, 1]],
                'grass': [[1, 1], [1, 1]], 'soliderPosition': [1, 1]})
save_game({'key_pressed': 3, 'mine_field': [[2, 2], [2, 2]],
                'grass': [[2, 2], [2, 2]], 'soliderPosition': [1, 1]})

import pandas
import os
import json

DATA_BASE_NAME = 'dataBase.csv'
data = {'key_pressed': [None],
        'mine_field': [None],
        'grass': [None],
        'soliderPosition': [None]
        }

data2={'key_pressed': ["None", "jhj"],
        'mine_field': ["nn", "hbh"],
        'grass': ["llll", "hghg"],
        'soliderPosition': ["None", "lklkl"]}
def init_data_base():
    if not os.path.exists(DATA_BASE_NAME):
        df = pandas.DataFrame(data,
                              columns=['key_pressed', 'mine_field', 'grass',
                                       'soliderPosition'])
        df.to_csv('database.csv', index=False)


def convert_data_lists_to_srt(game_data):
    for key in game_data.keys():
        if type(game_data[key]) is list:
            game_data[key] = json.dumps(game_data[key])
    return game_data


def save_game():
    """game_data_bs = convert_data_lists_to_srt(game_data)
    print(game_data_bs)"""
    df2 = pandas.DataFrame(data2)
    df = pandas.read_csv("database.csv")
    df=df.append(df2, ignore_index=True)
    print(df2)


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
save_game()
"""save_game({'key_pressed': 4, 'mine_field': [[1, 1], [1, 1]],
           'grass': [[1, 1], [1, 1]], 'soliderPosition': [1, 1]}, 0)
save_game({'key_pressed': 3, 'mine_field': [[2, 2], [2, 2]],
           'grass': [[2, 2], [2, 2]], 'soliderPosition': [1, 1]}, 1)
"""
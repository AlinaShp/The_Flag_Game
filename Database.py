import pandas
import os
import json

DATA_BASE_NAME = 'dataBase.csv'


def init_data_base():
    if not os.path.exists(DATA_BASE_NAME):
        df = pandas.DataFrame()
        df.to_csv(DATA_BASE_NAME, columns=['num_button_pressed','mine_field','grass','soliderPosition'], mode='w')



def convert_data_lists_to_srt(game_data):
    for key in game_data.keys():
        if type(game_data[key]) is list:
            game_data[key] = json.dumps(game_data[key])
    return game_data


def save_game(game_data):
    game_data = convert_data_lists_to_srt(game_data)
    new_data_frame = pandas.DataFrame([game_data])
    df = pandas.read_csv(DATA_BASE_NAME)
    if (df['num_button_pressed'] == game_data['num_button_pressed']).any():
        df.drop(index=df[df['num_button_pressed'] == game_data['num_button_pressed']].index, inplace=True)
        df.to_csv(DATA_BASE_NAME, mode='w', header=False)
    new_data_frame.to_csv(DATA_BASE_NAME, mode='a', header=False)


def get_game(num_button_pressed):
    df = pandas.read_csv(DATA_BASE_NAME)
    df2 = df[df['num_button_pressed'] == num_button_pressed]
    print(df2.to_string())


init_data_base()
# save_game({'num_button_pressed':0,'mine_field':[[1,1], [1,1]],'grass':[[1,1], [1,1]],'soliderPosition':[1,1]})
# save_game({'num_button_pressed':1,'mine_field':[[1,1], [1,1]],'grass':[[1,1], [1,1]],'soliderPosition':[1,1]})
# # # #get_game(0)
# # d = pandas.read_csv(DATA_BASE_NAME)
# print(df)
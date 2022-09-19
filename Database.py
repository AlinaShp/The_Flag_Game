import pandas
import os
import json

DATA_BASE_NAME = 'dataBase.csv'
DATA_FRAME = None


def init_data_base():
    if not os.path.exists(DATA_BASE_NAME):
        new_file = open(DATA_BASE_NAME, 'w')
        new_file.write('key_pressed,mine_field,grass, soliderPosition\n')
        new_file.close()


def convert_data_lists_to_srt(game_data):
    for key in game_data.keys():
        if type(game_data[key]) is list:
            game_data[key] = json.dumps(game_data[key])
    return game_data


def save_game(game_data, num_button_pressed):
    game_data = convert_data_lists_to_srt(game_data)
    # df = pandas.read_csv(DATA_BASE_NAME)
    # df.drop(index= df[df['key'] == num_button_pressed].index, inplace=True)
    # df.to_csv(DATA_BASE_NAME)
    new_data_frame = pandas.DataFrame([game_data])#, index=[num_button_pressed])
    new_data_frame.to_csv(DATA_BASE_NAME, mode='a', header=False)


def get_game(num_button_pressed):
    df = pandas.read_csv(DATA_BASE_NAME)
    df2 = df[df['key_pressed'] == num_button_pressed]
    print(df2.to_string())

init_data_base()
save_game({'key_pressed': 4,'mine_field':[[1,1], [1,1]],'grass':[[1,1], [1,1]],'soliderPosition':[1,1]},0)
save_game({'key_pressed':3, 'mine_field':[[2,2], [2,2]],'grass':[[2,2], [2,2]],'soliderPosition':[1,1]}, 1)
get_game(0)
DATA_FRAME = pandas.read_csv(DATA_BASE_NAME)
print(DATA_FRAME)
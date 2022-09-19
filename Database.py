import os
import json
import pandas as pd

DB = 'BD.csv'


def init_file():
    if not os.path.exists(DB):
        df = pd.DataFrame(columns=['Grass', 'LendMines', 'SoliderPlace'], index=[x for x in range(1, 10)])
        df.to_csv(DB)



def save_game_in_file(game_data, key_pressed_num):
    """
    save new game
    :param game_data: list of str objects  ['Grass', 'LendMines', 'SoliderPlace']
    :param key_pressed_num: int of key pressed, func is not responsible to check value
    :return: None
    """
    df = pd.read_csv(DB, index_col=0)
    df.loc[key_pressed_num] = game_data
    df.to_csv(DB)


def get_saved_game_from_file(key_pressed_num):
    key_pressed_num -= 1 # all indexes +1
    df = pd.read_csv(DB, index_col=0)
    df = df.iloc[key_pressed_num]
    list_game_data = df.values.tolist()
    if type(list_game_data[0]) is str:
        return list_game_data
    else: # nan var exist row is empty
        return False


def convert_list_items_to_str(data):
    for i in range(len(data)):
        data[i] = json.dumps(data[i])


def convert_list_items_to_list(data):
    for i in range(len(data)):
        data[i] = json.loads(data[i])


def main():

    game = [[[1,1,0],[1,1,0]],[[1,1,0],[1,1,0]],[1,2]]
    key_pressed = 1
    convert_list_items_to_str(game)

    init_file()
    save_game_in_file(game,key_pressed)

    game_r = get_saved_game_from_file(key_pressed)
    convert_list_items_to_list(game_r)
    print(game_r)


if __name__ == '__main__':
    main()

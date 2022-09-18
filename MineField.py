import consts
import random

MINE_FIELD_MATRIX = []


def insert_to_mine_field(new_obj, num_obj):
    count = 0
    while num_obj != count:
        random_x = random.randint(0, consts.SCREEN_GRID_HEIGHT-1)
        random_y = random.randint(0, consts.SCREEN_GRID_WIDTH-1)
        if MINE_FIELD_MATRIX[random_x][random_y] == consts.FREE:
            MINE_FIELD_MATRIX[random_x][random_y] = new_obj
            count += 1
    return MINE_FIELD_MATRIX


def create_mine_field():
    for row in range(consts.SCREEN_GRID_HEIGHT):
        temp_list = []
        for col in range(consts.SCREEN_GRID_WIDTH):
            temp_list.append(consts.FREE)
        MINE_FIELD_MATRIX.append(temp_list)
    return MINE_FIELD_MATRIX


def init_mine_field():
    create_mine_field()
    insert_to_mine_field()
    return MINE_FIELD_MATRIX


def player_win(player_x, player_y):
    return player_x+consts.PLAYER_SIZE[0] >= consts.FLAG_LOCATION[0] and\
           player_y+consts.PLAYER_SIZE[1] >= consts.FLAG_LOCATION[1]


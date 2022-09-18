import consts
import random

MINE_FIELD_MATRIX = []
GRASS_FIELD_MATRIX = []


def insert_to_mine_field(filed, new_obj, num_obj):
    count = 0
    while num_obj != count:
        random_x = random.randint(0, consts.SCREEN_GRID_HEIGHT-1)
        random_y = random.randint(0, consts.SCREEN_GRID_WIDTH-1)
        if filed[random_x][random_y] == consts.FREE:
            filed[random_x][random_y] = new_obj
            count += 1
    return filed


def create_field(filed):
    for row in range(consts.SCREEN_GRID_HEIGHT):
        temp_list = []
        for col in range(consts.SCREEN_GRID_WIDTH):
            temp_list.append(consts.FREE)
        filed.append(temp_list)
    return filed


def init_mine_field(matrix, new_obj, num_obj):
    return insert_to_mine_field(create_field(matrix), new_obj, num_obj)


def get_lend_mine_position(index_row, index_col):
    return index_row*consts.CELL_SIZE, index_col*consts.CELL_SIZE




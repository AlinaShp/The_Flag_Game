import pygame
import consts
import MineField

def soldier_move(key_pressed, soldier_rect):
    if key_pressed[pygame.K_DOWN] and soldier_rect.y + consts.CELL_SIZE < consts.SCREEN_HEIGHT-60:
        soldier_rect.y += consts.CELL_SIZE

    if key_pressed[pygame.K_UP] and soldier_rect.y - consts.CELL_SIZE > 0:
        soldier_rect.y -= consts.CELL_SIZE

    if key_pressed[pygame.K_LEFT] and soldier_rect.x - consts.CELL_SIZE > 0:
        soldier_rect.x -= consts.CELL_SIZE

    if key_pressed[pygame.K_RIGHT] and soldier_rect.x + consts.CELL_SIZE < consts.SCREEN_WIDTH-20:
        soldier_rect.x += consts.CELL_SIZE


def player_win(player_x, player_y):
    return player_x+consts.PLAYER_SIZE[0] >= consts.FLAG_LOCATION[0] and\
           player_y+consts.PLAYER_SIZE[1] >= consts.FLAG_LOCATION[1]


def get_feet_position(soldier_x, soldier_y):
    feet_x = soldier_x
    feet_y = soldier_y + consts.PLAYER_SIZE[1] - consts.CELL_SIZE
    return feet_x, feet_y


def did_hit_lend_mine(solider_feet_position, mine_position):
    return solider_feet_position[1] == mine_position[1] and \
           (solider_feet_position[0] == mine_position[0] or
            solider_feet_position[0] == mine_position[0] + consts.CELL_SIZE)


def player_loss(land_mains_matrix, solider_position_x, solider_position_y):
    feet_x, feet_y = get_feet_position(solider_position_x, solider_position_y)
    for row in range(consts.SCREEN_GRID_HEIGHT):
        for col in range(consts.SCREEN_GRID_WIDTH):
            if land_mains_matrix[row][col] == consts.MINE_FILE:
                if did_hit_lend_mine([feet_x, feet_y], MineField.get_lend_mine_position(row, col)):
                    return True
    return False

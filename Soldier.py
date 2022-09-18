import pygame
import consts


def soldier_move(key_pressed, soldier_rect):
    if key_pressed[pygame.K_DOWN] and soldier_rect.y + consts.CELL_SIZE < consts.SCREEN_HEIGHT-60:
        soldier_rect.y += consts.CELL_SIZE

    if key_pressed[pygame.K_UP] and soldier_rect.y - consts.CELL_SIZE > 0:
        soldier_rect.y -= consts.CELL_SIZE

    if key_pressed[pygame.K_LEFT] and soldier_rect.x - consts.CELL_SIZE > 0:
        soldier_rect.x -= consts.CELL_SIZE

    if key_pressed[pygame.K_RIGHT] and soldier_rect.x + consts.CELL_SIZE < consts.SCREEN_WIDTH-20:
        soldier_rect.x += consts.CELL_SIZE


def get_feet_position(soldier_x, soldier_y):
    feet_x = soldier_x
    feet_y = soldier_y + consts.PLAYER_SIZE[1] - consts.CELL_SIZE
    return feet_x, feet_y


def get_lend_mine_position(index_row, index_col):
    return index_row*consts.CELL_SIZE, index_col*consts.CELL_SIZE


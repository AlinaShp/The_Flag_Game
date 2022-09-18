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

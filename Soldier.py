import pygame
import consts

def soldier_move (key_pressed, soldier_rect):
    if key_pressed[pygame.K_DOWN]:
        soldier_rect.y += consts.CELL_SIZE
    if key_pressed[pygame.K_UP]:
        soldier_rect.y -= consts.CELL_SIZE
    if key_pressed[pygame.K_LEFT]:
        soldier_rect.x -= consts.CELL_SIZE
    if key_pressed[pygame.K_RIGHT]:
        soldier_rect.x += consts.CELL_SIZE
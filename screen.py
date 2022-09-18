import os.path
import pygame

import MineField
import Soldier
import consts

pygame.display.set_caption('the flag game')
WIN = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
FPS = 30
SOLDIER_IMG = pygame.image.load(os.path.join('soldier.png'))
SOLDIER_OBJ = pygame.transform.scale(SOLDIER_IMG, consts.PLAYER_SIZE)
FLAG_IMG = pygame.image.load(os.path.join('flag.png'))
FLAG_OBJ = pygame.transform.scale(FLAG_IMG, consts.FLAG_SIZE)
MINE_IMG = pygame.image.load(os.path.join('mine.png'))
MINE_OBJ = pygame.transform.scale(MINE_IMG, consts.LAND_MINES_SIZE)


def style_game(color, soldier_rect):
    WIN.fill(color)
    WIN.blit(SOLDIER_OBJ, (soldier_rect.x, soldier_rect.y))
    WIN.blit(FLAG_OBJ, (consts.FLAG_LOCATION[0], consts.FLAG_LOCATION[1]))
    WIN.blit(MINE_OBJ, (100, 100))

    pygame.display.update()


def screen_color_change(key_pressed, soldier_rect):
    style_game(consts.GREEN, soldier_rect)
    if key_pressed[pygame.K_RETURN]:
        style_game(consts.BLACK, soldier_rect)
        make_grid()
        draw_mines()
        pygame.time.wait(1000)
        style_game(consts.GREEN, soldier_rect)


def make_grid():
    for i in range(0, consts.SCREEN_WIDTH, consts.CELL_SIZE):
        pygame.draw.line(WIN, consts.WHITE, (0, i), (consts.SCREEN_WIDTH, i))
        pygame.draw.line(WIN, consts.WHITE, (i, 0), (i, consts.SCREEN_WIDTH))
    pygame.display.update()


def draw_mines():
    mine_field = MineField.init_mine_field(MineField.MINE_FIELD_MATRIX, consts.MINE_FILE, consts.NUM_LAND_MINES)
    for row in range(consts.SCREEN_GRID_HEIGHT):
        for col in range(consts.SCREEN_GRID_WIDTH):
            if mine_field[row][col] == consts.MINE_FILE:
                WIN.blit(MINE_OBJ, (col * consts.CELL_SIZE, row * consts.CELL_SIZE))

#def draw_grass():



def main():
    clock = pygame.time.Clock()
    state = True
    soldier_rect = pygame.Rect(0, 0, consts.PLAYER_SIZE[0],
                               consts.PLAYER_SIZE[1])
    while state:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = False
        key_pressed = pygame.key.get_pressed()
        screen_color_change(key_pressed, soldier_rect)
        Soldier.soldier_move(key_pressed, soldier_rect)

    pygame.quit()


if __name__ == "__main__":
    main()

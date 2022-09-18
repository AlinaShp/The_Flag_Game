import os.path
import pygame
import tkinter
import MineField
import Soldier
import consts

pygame.display.set_caption('the flag game')
WIN = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
FPS = 30
SOLDIER_IMG = pygame.image.load(os.path.join('soldier.png'))
SOLDIER_OBJ = pygame.transform.scale(SOLDIER_IMG, (80, 80))
FLAG_IMG = pygame.image.load(os.path.join('flag.png'))
FLAG_OBJ = pygame.transform.scale(FLAG_IMG, consts.FLAG_SIZE)
MINE_IMG = pygame.image.load(os.path.join('mine.png'))
MINE_OBJ = pygame.transform.scale(MINE_IMG, consts.LAND_MINES_SIZE)
GRASS_IMG = pygame.image.load(os.path.join('grass.png'))
GRASS_OBJ = pygame.transform.scale(GRASS_IMG, consts.GRASS_SIZE)


def style_game(color, soldier_rect, grass_field):
    WIN.fill(color)
    WIN.blit(SOLDIER_OBJ, (soldier_rect.x, soldier_rect.y))
    WIN.blit(FLAG_OBJ, (consts.FLAG_LOCATION[0], consts.FLAG_LOCATION[1]))
    draw_grass(grass_field)

    pygame.display.update()


def style_game_black(color, soldier_rect):
    WIN.fill(color)
    WIN.blit(SOLDIER_OBJ, (soldier_rect.x, soldier_rect.y))
    pygame.display.update()


def screen_color_change(key_pressed, soldier_rect, mine_field, grass_field):
    style_game(consts.GREEN, soldier_rect, grass_field)
    if key_pressed[pygame.K_RETURN]:
        style_game_black(consts.BLACK, soldier_rect)
        make_grid()
        draw_mines(mine_field)
        pygame.time.wait(1000)
        style_game(consts.GREEN, soldier_rect, grass_field)

def message_screen():
    FONT = "Calibri"
    FONT_SIZE = 30
    root = tkinter.Tk()
    root.geometry("300x200")
    root.title("Message")
    line1_label = tkinter.Label(root, text="YOU WON!", font=(FONT, FONT_SIZE))
    line1_label.place(x=60, y=60)
    root.mainloop()



def make_grid():
    for i in range(0, consts.SCREEN_WIDTH, consts.CELL_SIZE):
        pygame.draw.line(WIN, consts.WHITE, (0, i), (consts.SCREEN_WIDTH, i))
        pygame.draw.line(WIN, consts.WHITE, (i, 0), (i, consts.SCREEN_WIDTH))
    pygame.display.update()


def draw_mines(mine_field):
   # mine_field = MineField.MINE_FIELD_MATRIX
    for row in range(consts.SCREEN_GRID_HEIGHT):
        for col in range(consts.SCREEN_GRID_WIDTH):
            if mine_field[row][col] == consts.MINE_FILE:
                WIN.blit(MINE_OBJ,
                         (col * consts.CELL_SIZE, row * consts.CELL_SIZE))
    pygame.display.update()


def draw_grass(grass_field):
   # grass_field = MineField.GRASS_FIELD_MATRIX
    for row in range(consts.SCREEN_GRID_HEIGHT):
        for col in range(consts.SCREEN_GRID_WIDTH):
            if grass_field[row][col] == consts.GRASS:
                WIN.blit(GRASS_OBJ,
                         (col * consts.CELL_SIZE, row * consts.CELL_SIZE))
    pygame.display.update()




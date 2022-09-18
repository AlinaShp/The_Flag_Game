import os.path
import pygame
import consts

pygame.init()
pygame.font.init()
pygame.display.set_caption('the flag game')
WIN = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
SOLDIER_IMG = pygame.image.load(os.path.join('soldier.png'))
SOLDIER_OBJ = pygame.transform.scale(SOLDIER_IMG,consts.PLAYER_IMG_SIZE)
FLAG_IMG = pygame.image.load(os.path.join('flag.png'))
FLAG_OBJ = pygame.transform.scale(FLAG_IMG, consts.FLAG_SIZE)
MINE_IMG = pygame.image.load(os.path.join('mine.png'))
MINE_OBJ = pygame.transform.scale(MINE_IMG, consts.LAND_MINES_SIZE)
GRASS_IMG = pygame.image.load(os.path.join('grass.png'))
GRASS_OBJ = pygame.transform.scale(GRASS_IMG, consts.GRASS_SIZE)
END_MSG_FONT = pygame.font.SysFont('Verdana', 60)
START_MSG_FONT = pygame.font.SysFont('Verdana', 20)


def style_game(color, soldier_rect, grass_field, msg = ''):
    WIN.fill(color)
    WIN.blit(SOLDIER_OBJ, (soldier_rect.x, soldier_rect.y))
    WIN.blit(FLAG_OBJ, (consts.FLAG_LOCATION[0], consts.FLAG_LOCATION[1]))
    draw_grass(grass_field)
    msg_text_surface = START_MSG_FONT.render(msg, False, consts.WHITE)
    WIN.blit(msg_text_surface, (consts.PLAYER_IMG_SIZE[0],0))
    pygame.display.update()


def begin_msg():
    font = pygame.font.Font(None, 30)
    textsurface = font.render('Welcome to the flag game\n Have fun!', False, consts.WHITE)
    WIN.blit(textsurface,(80, 0))


def style_game_black(color, soldier_rect):
    WIN.fill(color)
    WIN.blit(SOLDIER_OBJ, (soldier_rect.x, soldier_rect.y))
    pygame.display.update()


def screen_color_change(key_pressed, soldier_rect, mine_field, grass_field):
    if key_pressed[pygame.K_RETURN]:
        style_game_black(consts.BLACK, soldier_rect)
        make_grid()
        draw_mines(mine_field)
        pygame.time.wait(1000)
        style_game(consts.GREEN, soldier_rect, grass_field)


def message_screen(str_state):
    WIN.fill(consts.WHITE)
    textsurface = END_MSG_FONT.render(str_state, False, consts.BLACK)
    WIN.blit(textsurface, textsurface.get_rect(center=WIN.get_rect().center))
    pygame.display.update()


def make_grid():
    for i in range(0, consts.SCREEN_WIDTH, consts.CELL_SIZE):
        pygame.draw.line(WIN, consts.WHITE, (0, i), (consts.SCREEN_WIDTH, i))
        pygame.draw.line(WIN, consts.WHITE, (i, 0), (i, consts.SCREEN_WIDTH))
    pygame.display.update()


def draw_mines(mine_field):
    for row in range(consts.SCREEN_GRID_HEIGHT):
        for col in range(consts.SCREEN_GRID_WIDTH):
            if mine_field[row][col] == consts.MINE_FILE:
                WIN.blit(MINE_OBJ,
                         (col * consts.CELL_SIZE, row * consts.CELL_SIZE))
    pygame.display.update()


def draw_grass(grass_field):
    for row in range(consts.SCREEN_GRID_HEIGHT):
        for col in range(consts.SCREEN_GRID_WIDTH):
            if grass_field[row][col] == consts.GRASS:
                WIN.blit(GRASS_OBJ,
                         (col * consts.CELL_SIZE, row * consts.CELL_SIZE))
    pygame.display.update()


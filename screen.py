import os.path
import pygame
import consts
import keyboard
import time


def create_img_obj(img_name, img_size):
    img = pygame.image.load(os.path.join(img_name))
    return pygame.transform.scale(img, img_size)


# general board
pygame.init()
pygame.display.set_caption('the flag game')
WIN = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
# all images obj
SOLDIER_OBJ = create_img_obj('soldier.png', consts.PLAYER_IMG_SIZE)
FLAG_OBJ = create_img_obj('flag.png', consts.FLAG_SIZE)
MINE_OBJ = create_img_obj('mine.png', consts.LAND_MINES_SIZE)
GRASS_OBJ = create_img_obj('grass.png', consts.GRASS_SIZE)
# messages style
pygame.font.init()
END_MSG_FONT = pygame.font.SysFont('Verdana', 60)
START_MSG_FONT = pygame.font.SysFont('Verdana', 20)


def style_game(color, soldier_rect, grass_field, msg=''):
    WIN.fill(color)
    WIN.blit(SOLDIER_OBJ, (soldier_rect.x, soldier_rect.y))
    WIN.blit(FLAG_OBJ, (consts.FLAG_LOCATION[0], consts.FLAG_LOCATION[1]))
    draw_objects(grass_field, GRASS_OBJ, consts.GRASS)
    msg_text_surface = START_MSG_FONT.render(msg, False, consts.WHITE)
    WIN.blit(msg_text_surface, (consts.PLAYER_IMG_SIZE[0], 0))
    pygame.display.update()


def style_game_black(color, soldier_rect):
    WIN.fill(color)
    WIN.blit(SOLDIER_OBJ, (soldier_rect.x, soldier_rect.y))
    pygame.display.update()


def screen_color_change(key_pressed, soldier_rect, mine_field, grass_field):
    style_game_black(consts.BLACK, soldier_rect)
    make_grid()
    draw_objects(mine_field, MINE_OBJ, consts.LAND_MINE)
    pygame.time.wait(1000)
    pygame.event.clear()
    style_game(consts.GREEN, soldier_rect, grass_field)





def message_screen(str_state):
    WIN.fill(consts.WHITE)
    text_surface = END_MSG_FONT.render(str_state, False, consts.BLACK)
    WIN.blit(text_surface, text_surface.get_rect(center=WIN.get_rect().center))
    pygame.display.update()


def make_grid():
    for i in range(0, consts.SCREEN_WIDTH, consts.CELL_SIZE):
        pygame.draw.line(WIN, consts.WHITE, (0, i), (consts.SCREEN_WIDTH, i))
        pygame.draw.line(WIN, consts.WHITE, (i, 0), (i, consts.SCREEN_WIDTH))
    pygame.display.update()


def draw_objects(field, img_obj, obj_const):
    for row in range(consts.SCREEN_GRID_HEIGHT):
        for col in range(consts.SCREEN_GRID_WIDTH):
            if field[row][col] == obj_const:
                WIN.blit(img_obj, (col * consts.CELL_SIZE, row * consts.CELL_SIZE))
    pygame.display.update()


def is_num_pressed(key):
    return (key == pygame.K_1 or key == pygame.K_2 or key == pygame.K_3 or
            key == pygame.K_4 or key == pygame.K_5 or key == pygame.K_6
            or key == pygame.K_7 or key == pygame.K_8 or key == pygame.K_9)




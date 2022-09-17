import os.path

import pygame
import consts

pygame.display.set_caption('the flag game')
WIN = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
FPS = 60
SOLDIER_IMG = pygame.image.load(os.path.join('soldier.png'))
SOLDIER_OBJ = pygame.transform.scale(SOLDIER_IMG, consts.PLAYER_SIZE)


def style_game(color, soldier_rect):
    wind = WIN
    WIN.fill(color)
    WIN.blit(SOLDIER_OBJ, (soldier_rect.x, soldier_rect.y))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    state = True
    soldier_rect = pygame.Rect(0, 0, consts.PLAYER_SIZE[0],consts.PLAYER_SIZE[1])
    while state:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = False
        style_game(consts.GREEN, soldier_rect)
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RETURN]:
            style_game(consts.BLACK, soldier_rect)
            pygame.time.wait(1000)
            style_game(consts.GREEN, soldier_rect)
        if key_pressed[pygame.K_DOWN]:
            soldier_rect.y += consts.CELL_SIZE
        if key_pressed[pygame.K_UP]:
            soldier_rect.y -= consts.CELL_SIZE
        if key_pressed[pygame.K_LEFT]:
            soldier_rect.x -= consts.CELL_SIZE
        if key_pressed[pygame.K_RIGHT]:
            soldier_rect.x += consts.CELL_SIZE

        """if key_pressed[pygame.K_DOWN]:
            style_game()"""

    pygame.quit()


if __name__ == "__main__":
    main()

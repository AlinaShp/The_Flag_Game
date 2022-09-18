import pygame
import screen
import consts
import Soldier
import MineField

state = {'state': True, 'mine_field': None, 'grass': None, 'soldier_rect': None}


def main():
    clock = pygame.time.Clock()
    state['soldier_rect'] = pygame.Rect(0, 0, consts.PLAYER_SIZE[0],consts.PLAYER_SIZE[1])
    while state['state']:
        clock.tick(consts.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state['state'] = False
        key_pressed = pygame.key.get_pressed()
        screen.screen_color_change(key_pressed, state['soldier_rect'])
        Soldier.soldier_move(key_pressed, state['soldier_rect'])

    pygame.quit()


if __name__ == "__main__":
    main()

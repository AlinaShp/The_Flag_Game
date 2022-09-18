import pygame
import screen
import consts
import Soldier
import MineField
import time

state = {'state': True,
         'mine_field': MineField.init_mine_field(MineField.MINE_FIELD_MATRIX,
                                                 consts.MINE_FILE,
                                                 consts.NUM_LAND_MINES),
         'grass': MineField.init_mine_field(MineField.GRASS_FIELD_MATRIX,
                                            consts.GRASS, consts.NUM_GRASS),
         'soldier_rect': None}


def main():
    clock = pygame.time.Clock()
    state['soldier_rect'] = pygame.Rect(0, 0, consts.PLAYER_SIZE[0],
                                        consts.PLAYER_SIZE[1])
    while state['state']:
        clock.tick(consts.FPS)
        key_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state['state'] = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                Soldier.soldier_move(key_pressed, state['soldier_rect'])
            screen.screen_color_change(key_pressed, state['soldier_rect'],
                                       state['mine_field'], state['grass'])

<<<<<<< HEAD
        if MineField.player_win(state['soldier_rect'].x,
                                state['soldier_rect'].y):
            screen.message_screen()
            print('win')  # chang to new screen
            time.sleep(3)
=======

        if Soldier.player_win(state['soldier_rect'].x, state['soldier_rect'] .y):
            print('win') # chang to new screen
            pygame.time.wait(3000)
            state['state'] = False
        elif Soldier.player_loss(state['mine_field'], state['soldier_rect'].x, state['soldier_rect'].y):
            print('lost')  # chang to new screen
            pygame.time.wait(3000)
>>>>>>> 109810608e1900cddda9241568141fc69908f9d2
            state['state'] = False


    pygame.quit()


if __name__ == "__main__":
    main()

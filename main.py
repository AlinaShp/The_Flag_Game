import pygame
import screen
import consts
import Soldier
import MineField

state = {'state': True,
         'mine_field': MineField.init_mine_field(consts.LAND_MINE, consts.NUM_LAND_MINES),
         'grass': MineField.init_mine_field(consts.GRASS, consts.NUM_GRASS),
         'soldier_rect': pygame.Rect(0, 0, consts.PLAYER_SIZE[0], consts.PLAYER_SIZE[1])}



def main():
    clock = pygame.time.Clock()
    screen.style_game(consts.GREEN, state['soldier_rect'], state['grass'], "Welcome to The Flag game. Have Fun!")
    while state['state']:
        clock.tick(consts.FPS)
        key_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state['state'] = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if screen.cond(key_pressed):
                    print("Yes")
                   # print(screen.pressing_numbers(key_pressed))

                Soldier.soldier_move(key_pressed, state['soldier_rect'])
                screen.style_game(consts.GREEN, state['soldier_rect'], state['grass'])



            screen.screen_color_change(key_pressed, state['soldier_rect'], state['mine_field'], state['grass'])

        if Soldier.player_win(state['soldier_rect'].x, state['soldier_rect'] .y):
            screen.message_screen("YOU WON!")
            pygame.time.wait(3000)
            state['state'] = False
        elif Soldier.player_loss(state['mine_field'], state['soldier_rect'].x, state['soldier_rect'].y):
            screen.message_screen("You lost :(")
            pygame.time.wait(3000)
            state['state'] = False



    pygame.quit()


if __name__ == "__main__":
    main()

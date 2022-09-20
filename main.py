import pygame
import screen
import consts
import Soldier
import MineField
import time
import Database

Database.init_file()
state = {'state': True,
         'mine_field': MineField.init_mine_field(consts.LAND_MINE, consts.NUM_LAND_MINES),
         'grass': MineField.init_mine_field(consts.GRASS, consts.NUM_GRASS),
         'soldier_rect': pygame.Rect(0, 0, consts.PLAYER_SIZE[0], consts.PLAYER_SIZE[1]),
         'start_time': None}


def check_time_update_data(time, key_pressed):
    game_data = [state['grass'], state['mine_field'], [state["soldier_rect"].x, state["soldier_rect"].y]]
    if abs(time) <= 1:
        new_data = Database.get_saved_game_from_file(key_pressed-48)
        if new_data:
            save_parameters_to_main(new_data)
            screen.style_game(consts.GREEN, state['soldier_rect'], state['grass'])
        else:
            screen.style_game(consts.GREEN, state['soldier_rect'], state['grass'], "doesnt have data")
    else:
        Database.save_game_in_file(game_data, key_pressed-48)


def save_parameters_to_main(list_game_data):
    state['mine_field'] = list_game_data[1]
    state['grass'] = list_game_data[0]
    state['soldier_rect'] = pygame.Rect(list_game_data[2][0],
                                        list_game_data[2][1],consts.PLAYER_SIZE[0],consts.PLAYER_SIZE[1])


def main():
    clock = pygame.time.Clock()
    screen.style_game(consts.GREEN, state['soldier_rect'], state['grass'], "Welcome to The Flag game. Have Fun!")

    while state['state']:
        clock.tick(consts.FPS)
        key_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state['state'] = False
            elif event.type == pygame.KEYDOWN:
                if Soldier.soldier_move(event.key, state['soldier_rect']):
                    screen.style_game(consts.GREEN, state['soldier_rect'], state['grass'])
                elif screen.is_num_pressed(event.key):
                    state['start_time'] = time.time()
            elif event.type == pygame.KEYUP:
                if screen.is_num_pressed(event.key):
                    end_time = time.time()
                    check_time_update_data(state['start_time'] - end_time, event.key)

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

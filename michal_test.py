import pygame
import consts
pygame.display.set_caption('the flag game')
WIN = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
FPS = 60

def style_game(wind = WIN, color = consts.GREEN):
    wind.fill(color)
    pygame.display.update()

"""def main():
    clock = pygame.time.Clock()
    state = True
    style_game()
    while state:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = False
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            style_game(color=consts.BLACK)
        if key_pressed[pygame.K_DOWN]:
            style_game()



    pygame.quit()


if __name__ == "__main__":
    main()"""

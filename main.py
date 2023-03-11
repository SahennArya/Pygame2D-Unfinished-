import pygame
from settings import * #imports everyting from settings.py
from tiles import Tile
from level import Level
from player import Player

#1:10:08 https://www.youtube.com/watch?v=YWN8GcmJ-jA

screen = pygame.display.set_mode((WIDTH, HEIGHT)) #sets the dimensions of the window
clock = pygame.time.Clock() #gets the clock speed so we can later restrict the game to 60fps (line 17)
level = Level(level_map,screen)

def main():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        bg_image = pygame.image.load("bg/bg(2).jpg")
        bg_image = pygame.transform.scale(bg_image,(WIDTH,HEIGHT))
        screen.blit(bg_image,(0,0))
        level.run()

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
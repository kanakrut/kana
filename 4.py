import pygame 
import math
pygame.init()
black = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 255)

gamedisplay = pygame.display.set_mode((1080, 720))
screenSize = gamedisplay.get_size()        
background = pygame.Surface(screenSize) 
background.fill((0,0,0))                
background = background.convert()

pygame.draw.arc(background, RED, (0, 0, screenSize[0]*2, (screenSize[1]*2.1)), 0, 1000)

gamedisplay.blit(background, (0, 0))
pygame.display.flip()
pygame.display.set_caption("Ex4")
def run_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()
        

run_game()
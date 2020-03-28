import pygame 

pygame.init()
black = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 255)



gameDisplay = pygame.display.set_mode((800, 600))
gameDisplay.fill(black)
pygame.draw.circle(gameDisplay, RED, (400, 300), 300)
pygame.display.set_caption("Ex1")

def run_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()
        

run_game()
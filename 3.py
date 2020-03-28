import pygame 

pygame.init()
black = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 255)

gameDisplay = pygame.display.set_mode((600, 600))
gameDisplay.fill(black)
pygame.draw.line(gameDisplay, RED, (100, 500), (295, 100), 5)
pygame.draw.line(gameDisplay, RED, (295, 100), (500, 500), 5)
pygame.draw.line(gameDisplay, RED, (500, 500), (20, 225), 5)
pygame.draw.line(gameDisplay, RED, (20, 225), (575, 225), 5)
pygame.draw.line(gameDisplay, RED, (575, 225), (100, 500), 5)
pygame.display.set_caption("Ex3")
def run_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()
        

run_game()
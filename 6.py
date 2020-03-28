import pygame 

pygame.init()
screen = pygame.display.set_mode((800, 600)) 

gamedisplay = screen.get_size()         
background = pygame.Surface(gamedisplay) 
background.fill((0,0,0))   
pygame.display.set_caption("Ex6")              

for point in range(0, 641, 64):
    pygame.draw.line(background, (0, 128, 0), (0, 0), (gamedisplay[0]//2, point), 1)

for point in range(0, 641, 64):
    pygame.draw.line(background, (0, 0, 128), (gamedisplay[0], 0), (gamedisplay[0]//2, point), 1)

for point in range(0, 641, 64):
    pygame.draw.line(background, (255, 0, 0), (0, gamedisplay[1]), (gamedisplay[0]//2, point), 1)
    
for point in range(0, 641, 64):
    pygame.draw.line(background, (255, 255, 0), (gamedisplay[0], gamedisplay[1]), (gamedisplay[0]//2, point), 1)
    
screen.blit(background, (0, 0))
def run_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()
        

run_game()        
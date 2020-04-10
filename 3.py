import pygame
W = 1080
H = 720  
WHITE = (255, 255, 255)
RED = (255, 0, 0)
 
pygame.init()
game_display = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
 

x = W // 2
y = H // 2
r = 25
 
while True:
    game_display.fill(WHITE)
 
    pygame.draw.circle(game_display, RED, (x, y), r)
    
    
    pygame.display.update()
 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT and x >= 50:
                x -= 20
            elif i.key == pygame.K_RIGHT and x <= 1030:
                x += 20
            elif i.key == pygame.K_UP and y > 40:
                y -= 20
            elif i.key == pygame.K_DOWN and y < 680:
                y += 20
            
            
 
    clock.tick(60)
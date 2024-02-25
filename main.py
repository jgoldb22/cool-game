import pygame 

pygame.init()
clock = pygame.time.Clock()
background_colour = (234, 212, 252) 
screen = pygame.display.set_mode((300, 300)) 
pygame.display.set_caption('sex') 
screen.fill(background_colour) 
dt = 0
color = (155,30,220)
pygame.display.flip() 
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
running = True
  
while running: 
    
    for event in pygame.event.get():    
        if event.type == pygame.QUIT: 
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y = max(player_pos.y  - 3, 0)
    if keys[pygame.K_s]:
        player_pos.y = min(player_pos.y  + 3, screen.get_height()- 1)
    if keys[pygame.K_a]:
        player_pos.x = max(player_pos.x  - 3, 0)
    if keys[pygame.K_d]:
        player_pos.x = min(player_pos.x  + 3, screen.get_width() -1)
    if keys[pygame.K_y]:
        screen.fill(background_colour) 
        
    pygame.draw.rect(screen, color, pygame.Rect(player_pos.x, player_pos.y, 4, 4))
    pygame.display.flip()
    dt = clock.tick(60) / 1000
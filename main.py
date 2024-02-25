import pygame 
import random
from collectibles import *

pygame.init()
clock = pygame.time.Clock()
background_colour = (234, 212, 252) 
screen = pygame.display.set_mode((300, 300)) 
pygame.display.set_caption('sex') 
screen.fill(background_colour) 
dt = 0
color = (155,30,220)
color1 = (255,0,0)
count = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
pygame.display.flip() 
running = True

circle_pos = pygame.Vector2(screen.get_width() / 2, 0)
while running: 
    
    for event in pygame.event.get():    
        if event.type == pygame.QUIT: 
            running = False
    screen.fill(background_colour) 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y = max(player_pos.y  - 3, 0)
    if keys[pygame.K_s]:
        player_pos.y = min(player_pos.y  + 3, screen.get_height()- 1)
    if keys[pygame.K_a]:
        player_pos.x = max(player_pos.x  - 3, 0)
    if keys[pygame.K_d]:
        player_pos.x = min(player_pos.x  + 3, screen.get_width() -1)
    if (circle_pos.y == 0):
        circle_pos.x = random.randint(0, screen.get_width())
    circle_pos.y = (circle_pos.y + 3) % screen.get_height()
    pygame.draw.circle(screen, color1, circle_pos, 3)
    player = pygame.Rect(player_pos.x, player_pos.y, 20, 4)
    pygame.draw.rect(screen, color, player)
    pygame.display.flip()
    count = pygame.time.get_ticks() / 100
    dt = clock.tick(60) / 10000
    print(hello())
    # hello1
    

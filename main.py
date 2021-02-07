import pygame, sys
from os import path

pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

# Loading background image
bg_img = pygame.image.load(path.join('assets', 'background-day.png'))
bg_surface = pygame.transform.scale2x(bg_img)

# Main loop of the game
while True:
    for event in pygame.event.get(): 
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()   
    # Update the default surface to show the bg image.
    screen.blit(bg_surface,(0, 0))
    pygame.display.update()
    clock.tick(120)















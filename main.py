import pygame, sys
from os import path

pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()


def draw_floor():
    screen.blit(floor_surface,(floor_x_pos, 900))
    screen.blit(floor_surface,(floor_x_pos + 576, 900))


# Load and convert background image
bg_img = pygame.image.load(path.join('assets', 'background-day.png')).convert()
floor_img = pygame.image.load(path.join('assets', 'base.png')).convert()

# Scale the imported images
bg_surface = pygame.transform.scale2x(bg_img)
floor_surface = pygame.transform.scale2x(floor_img)

# Animate background movement
floor_x_pos = 0


# Main loop of the game
while True:
    for event in pygame.event.get(): 
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()

    # Update the default surface to show the bg image.
    screen.blit(bg_surface,(0, 0))
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0


    pygame.display.update()
    clock.tick(120)














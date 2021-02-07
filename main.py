import pygame, sys
from os import path

pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

# Game variables
gravity = 0.25 
bird_movement = 0
bird_jump = 12

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos, 900))
    screen.blit(floor_surface,(floor_x_pos + 576, 900))


# Load and convert background image
bg_img = pygame.image.load(path.join('assets', 'background-day.png')).convert()
floor_img = pygame.image.load(path.join('assets', 'base.png')).convert()
bird_img = pygame.image.load(path.join('assets', 'redbird-midflap.png')).convert()

# Scale the imported images
bg_surface = pygame.transform.scale2x(bg_img)
floor_surface = pygame.transform.scale2x(floor_img)
bird_surface = pygame.transform.scale2x(bird_img)

# Create rect from surface
bird_rect = bird_surface.get_rect(center = (100, 512))

# Animate background movement
floor_x_pos = 0


# Main loop of the game
while True:
    for event in pygame.event.get(): 
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_SPACE:
               bird_movement = 0 
               bird_movement -= bird_jump
    # Bird movement animation
    bird_movement += gravity  
    bird_rect.centery += bird_movement




    # Update the default surface to show the bg image.
    screen.blit(bg_surface,(0, 0))
    screen.blit(bird_surface, bird_rect)
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0


    pygame.display.update()
    clock.tick(120)














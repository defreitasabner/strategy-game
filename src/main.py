import random

import pygame

from constants import colors, settings

pygame.init()

# Setting up screen
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

# Actors
player = pygame.Rect((300, 250, 25, 25))
obstacles = []
for _ in range(10):
    obstacle_rect = pygame.Rect((random.randint(0, 500), random.randint(0, 300), 25, 25))
    obstacles.append(obstacle_rect)

# Game Loop
game_run = True
while game_run:

    # Cleaning screen
    screen.fill(colors.BACKGROUND)
    
    # Handling events
    player_color = colors.GREEN
    if player.collidelist(obstacles) >= 0:
        player_color = colors.RED

    # Drawing actors
    pygame.draw.rect(screen, player_color, player)
    for obstacle in obstacles:
        pygame.draw.rect(screen, colors.BLUE, obstacle)

    # Check player movements
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-1, 0)
    elif key[pygame.K_d]:
        player.move_ip(1, 0)
    elif key[pygame.K_w]:
        player.move_ip(0, -1)
    elif key[pygame.K_s]:
        player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False

    # Update screen
    pygame.display.flip()

pygame.quit()
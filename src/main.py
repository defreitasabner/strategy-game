import random

import pygame
import numpy as np

from constants import colors, settings
from models.scenario import Scenario

pygame.init()

# Setting up screen
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

# Scenario
scenario = Scenario(n_columns= 25, n_rows= 25)

# Actors
player = pygame.Rect((300, 250, 25, 25))
obstacles = []
for _ in range(10):
    obstacle_rect = pygame.Rect((random.randint(0, 500), random.randint(0, 300), 25, 25))
    obstacles.append(obstacle_rect)

# Variables
player_selected = False
movement = None
partial_movement = None
is_moving = False

# Game Loop
game_run = True
while game_run:

    # Cleaning screen
    screen.fill(colors.BACKGROUND)

    scenario.draw_grid_cells(screen)
    scenario.draw_grid_lines(screen)
    
    mouse_pos = pygame.mouse.get_pos()
    mouse_left_clicked = pygame.mouse.get_pressed()[0]
    mouse_right_clicked = pygame.mouse.get_pressed()[2]

    # Handling events
    player_color = colors.GREEN
    if player.collidelist(obstacles) >= 0:
        player_color = colors.RED
    if player.collidepoint(mouse_pos):
        player_color = colors.WHITE
        if mouse_left_clicked:
            player_selected = True
    if mouse_left_clicked and not player.collidepoint(mouse_pos):
        player_selected = False

    # Drawing actors
    pygame.draw.rect(screen, player_color, player)
    for obstacle in obstacles:
        pygame.draw.rect(screen, colors.BLUE, obstacle)
    if player_selected:
        pygame.draw.circle(screen, colors.WHITE, player.center, 25, 2)

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
    
    if player_selected and mouse_right_clicked:
        target_pos = np.array(pygame.mouse.get_pos())
        np_player_pos = np.array(player.center)
        movement = tuple(target_pos - np_player_pos)
        is_moving = True

    if is_moving:
        pygame.draw.circle(screen, colors.RED, target_pos, 10, 2)
        pygame.draw.line(screen, colors.RED, player.center, target_pos)
        if player.center != tuple(target_pos):
            player.move_ip(movement)
        else:
            is_moving = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False

    # Update screen
    pygame.display.flip()

pygame.quit()
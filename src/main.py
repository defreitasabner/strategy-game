import random

import pygame
import numpy as np

from constants import colors, settings
from models.scenario import Scenario

pygame.init()

# Set up
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Scenario
scenario = Scenario(size = 25)

# Actors
player = pygame.Rect((300, 250), (25, 25))
player.center = scenario.get_center_position_from_matrix_cell((1,1))
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
running = True
while running:

    # FPS control
    clock.tick(settings.FPS)

    # Cleaning screen
    screen.fill(colors.BLACK)

    scenario.draw(screen)
    scenario.draw_grid(screen)
    
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
        target_cell = scenario.get_matrix_cell_from_pixel_position(target_pos)
        target_cell_center = np.array(scenario.get_center_position_from_matrix_cell(target_cell))
        np_player_pos = np.array(player.center)
        movement = tuple(target_cell_center - np_player_pos)
        is_moving = True

    if is_moving:
        pygame.draw.circle(screen, colors.RED, target_pos, 10, 2)
        pygame.draw.line(screen, colors.RED, player.center, target_pos)
        if player.center != tuple(target_cell_center):
            player.move_ip(movement)
        else:
            is_moving = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update screen
    pygame.display.flip()

pygame.quit()
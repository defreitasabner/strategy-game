from typing import Tuple

import pygame
import numpy as np

from constants import settings, colors
from constants.types import MatrixPosition, PixelPosition

class Scenario:
    def __init__(self, size: int) -> None:
        self.matrix = self.generate_matrix(size)
        self.cell_width = settings.SCREEN_WIDTH // size
        self.cell_height = settings.SCREEN_HEIGHT // size

    def generate_matrix(self, size):
        matrix = np.array( [np.zeros(size, dtype= int) for i in range(size)] )
        return matrix

    def draw_grid(self, screen):
        temp_x = 0
        temp_y = 0
        for _ in range(self.matrix.shape[0]):
            temp_x += self.cell_width
            temp_y += self.cell_height
            pygame.draw.line(screen, colors.WHITE, (0, temp_y), (settings.SCREEN_WIDTH, temp_y))
            pygame.draw.line(screen, colors.WHITE, (temp_x, 0), (temp_x, settings.SCREEN_HEIGHT))

    def draw(self, screen):
        temp_x = 0
        temp_y = 0
        for i in range(self.matrix.shape[0]):
            for j in range(self.matrix.shape[1]):
                if self.matrix[i][j] == 0:
                    pygame.draw.rect(screen, colors.BLACK, (temp_x, temp_y, self.cell_width, self.cell_height))
                elif self.matrix[i][j] == 1:
                    pygame.draw.rect(screen, colors.BLACK, (temp_x, temp_y, self.cell_width, self.cell_height))
                temp_x += self.cell_width
            temp_x = 0
            temp_y += self.cell_height

    def get_center_position_from_matrix_cell(self, position: MatrixPosition) -> PixelPosition:
        x = ((position[1] + 1) * self.cell_width) - (self.cell_width // 2)
        y = ((position[0] + 1) * self.cell_height) - (self.cell_height // 2)
        return (x, y)
    
    def get_matrix_cell_from_pixel_position(self, position: PixelPosition) -> MatrixPosition:
        column = position[0] // self.cell_width
        row =  position[1] // self.cell_height
        return (row, column)

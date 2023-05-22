import pygame
import numpy as np

from constants import settings, colors

class Scenario:
    def __init__(self, size: int) -> None:
        self.matrix = self.generate_matrix(size)
        self.cell_width = settings.SCREEN_WIDTH // size
        self.cell_height = settings.SCREEN_HEIGHT // size

    def generate_matrix(self, size):
        matrix = np.array( [np.zeros(size, dtype= int) if i % 2 else np.ones(size, dtype= int) for i in range(size)] )
        return matrix

    def draw_grid_lines(self, screen):
        '''
        This method draw the lines of grid, without processing the cells.
        '''
        temp_x = 0
        temp_y = 0
        for _ in range(self.matrix.shape[0]):
            temp_x += self.cell_width
            temp_y += self.cell_height
            pygame.draw.line(screen, colors.WHITE, (0, temp_y), (settings.SCREEN_WIDTH, temp_y))
            pygame.draw.line(screen, colors.WHITE, (temp_x, 0), (temp_x, settings.SCREEN_HEIGHT))

    def draw_grid_cells(self, screen):
        '''
        This method draws grid cells and processing different types of cell based on matrix.
        '''
        temp_x = 0
        temp_y = 0
        for i in range(self.matrix.shape[0]):
            for j in range(self.matrix.shape[1]):
                if self.matrix[i][j] == 0:
                    pygame.draw.rect(screen, colors.RED, (temp_x, temp_y, self.cell_width, self.cell_height))
                elif self.matrix[i][j] == 1:
                    pygame.draw.rect(screen, colors.BACKGROUND, (temp_x, temp_y, self.cell_width, self.cell_height))
                temp_x += self.cell_width
            temp_x = 0
            temp_y += self.cell_height

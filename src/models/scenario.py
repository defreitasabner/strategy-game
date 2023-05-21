import pygame

from constants import settings, colors

class Scenario:
    def __init__(self, n_columns: int, n_rows: int) -> None:
        self.n_columns = n_columns
        self.n_rows = n_rows
        self.cell_width = settings.SCREEN_WIDTH // n_columns
        self.cell_height = settings.SCREEN_HEIGHT // n_rows

    def draw(self, screen):
        temp_x = 0
        temp_y = 0
        for _ in range(self.n_rows):
            temp_x += self.cell_width
            temp_y += self.cell_height
            # Lines
            pygame.draw.line(screen, colors.WHITE, (0, temp_y), (settings.SCREEN_WIDTH, temp_y))
            # Columns
            pygame.draw.line(screen, colors.WHITE, (temp_x, 0), (temp_x, settings.SCREEN_HEIGHT))

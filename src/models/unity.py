import pygame

from constants import unities
from constants.types import MatrixPosition

class Unity:
    def __init__(self, initial_position: MatrixPosition) -> None:
        self.row, self.column = initial_position
        self.rect = pygame.Rect((initial_position), (unities.STANDARD_DIMENSION))

    def get_current_position_on_matrix(self) -> MatrixPosition:
        return (self.row, self.column)

    def move(self, target_position: MatrixPosition):
        pass

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

    def event_handler(self, keys) -> None:
        pass
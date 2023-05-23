import pygame

from constants import unities

class Unity:
    def __init__(self, initial_position: tuple(float)) -> None:
        self.row
        self.column
        self.rect = pygame.Rect((initial_position), (unities.STANDARD_DIMENSION))

    def get_position_on_matrix(self) -> tuple(int):
        return (self.row, self.column)

    def move(self, target_position):
        pass

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

    def event_handler(self, keys) -> None:
        pass
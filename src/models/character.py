import pygame

class Character:
    def __init__(self, init_pos_x: float, init_pos_y: float, width: float, height: float) -> None:
        self.pos_x
        self.pos_y
        self.width
        self.height
        self.rect = pygame.Rect((self.pos_x, self.pos_y, self.width, self.height))

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

    def event_handler(self, keys) -> None:
        if keys[pygame.K_a]:
            self.rect.move_ip(-1, 0)
        elif keys[pygame.K_d]:
            self.rect.move_ip(1, 0)
        elif keys[pygame.K_w]:
            self.rect.move_ip(0, -1)
        elif keys[pygame.K_s]:
            self.rect.move_ip(0, 1)
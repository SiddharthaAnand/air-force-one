import random
import pygame
from pygame.locals import (
    RLEACCEL
)


class Cloud(pygame.sprite.Sprite):
    def __init__(self, screen_width=500, screen_height=500):
        super(Cloud, self).__init__()
        self.surface = pygame.image.load('assets/cloud.png').convert()
        self.surface.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surface.get_rect(
            center=(
                random.randint(screen_width + 20, screen_width + 100),
                random.randint(0, screen_height),
            )
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.left < 0:
            self.kill()


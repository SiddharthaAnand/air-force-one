import pygame
import random
from pygame.locals import (
    RLEACCEL
)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width=500, screen_height=500):
        super(Enemy, self).__init__()
        # .convert() - helps pygame render more quickly on non-accelerated
        # displays
        self.surface = pygame.image.load("assets/missile.png").convert()
        # The color of the background image which pygame will
        # render as transparent since that is the background
        # color of the image/missile
        self.surface.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surface.get_rect(
            center=(
                random.randint(screen_width + 20, screen_width + 100),
                random.randint(0, screen_height)
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

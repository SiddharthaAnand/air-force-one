import pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)

# Defining a Player Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width=500, screen_height=500):
        super(Player, self).__init__()
        self.surface = pygame.image.load("assets/jet.png").convert()
        self.surface.set_colorkey((255, 255, 255), RLEACCEL)
        # load image for player

        # use this to draw a player later
        self.rect = self.surface.get_rect()
        self.screen_height = screen_height
        self.screen_width = screen_width

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height



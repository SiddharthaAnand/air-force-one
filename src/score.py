import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super(Score, self).__init__()
        self.surface = pygame.Surface((10, 10))
        # self.surface.fill((0, 255, 255))
        self.rect = self.surface.get_rect()
        # self.surface.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surface.get_rect()
        self.font = pygame.font.SysFont("Courier", 20)
        # The color of the background image which pygame will
        # render as transparent since that is the background
        # color of the image/missile




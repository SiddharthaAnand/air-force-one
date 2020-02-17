import pygame
import json


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super(Score, self).__init__()
        self.surface = pygame.Surface((10, 10))
        # self.surface.fill((0, 255, 255))
        self.rect = self.surface.get_rect()
        # self.surface.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surface.get_rect()
        self.font = pygame.font.SysFont("Courier", 30)
        self.value = 0
        # The color of the background image which pygame will
        # render as transparent since that is the background
        # color of the image/missile

    def increment_value(self, jump=1):
        self.value = self.value + jump

    def get_value(self):
        return self.value


class HighScore(pygame.sprite.Sprite):
    def __init__(self):
        super(HighScore, self).__init__()
        self.surface = pygame.Surface((10, 10))
        # self.surface.fill((0, 255, 255))
        self.rect = self.surface.get_rect()
        # self.surface.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surface.get_rect()
        self.font = pygame.font.SysFont("Courier", 30)
        try:
            self.file = open('high_score', 'r')
            self.value = json.load(self.file)
            if self.value is not None:
                self.data = self.value
            else:
                self.data = {'high_score': [0]}
            self.file.close()
        except:
            pass

        # The color of the background image which pygame will
        # render as transparent since that is the background
        # color of the image/missile

    def write(self, data):
        if int(self.data['high_score'][0]) < data:
            fp = open('high_score', 'w')
            self.data['high_score'] = [data]
            json.dump(self.data, fp)
            fp.close()

    def get_value(self):
        return self.data['high_score'][0]




import pygame
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT,)


class Game(object):
    def __init__(self, name=None, screen=None):
        """Initialization"""
        self.name = name
        self.screen = screen

    def create_window(self, screen_width=500, screen_height=500):
        """Create a sample window where the game will run."""
        pygame.init()
        self.screen = pygame.display.set_mode([screen_width, screen_height])

    def start_game_loop(self):
        # Run until the user asks to quit
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.type == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False
            self.screen.fill([255, 255, 255])
            surface = pygame.Surface((50, 50))
            surface.fill((0, 0, 0))
            rect = surface.get_rect()
            self.screen.blit(surface, (400, 250))
            pygame.display.flip()

        pygame.quit()

    @staticmethod
    def get_random_color():
        import random
        return random.randint(1, 255)


if __name__ == '__main__':
    window = Game('air-force-one')
    window.create_window(800, 500)
    window.start_game_loop()

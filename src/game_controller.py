import pygame
from score import Score
from cloud import Cloud
from missile import Enemy
from jet import Player
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


class Game(object):
    def __init__(self, name=None,
                 screen_width=500,
                 screen_height=500):
        self.name = name
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        pygame.init()
        self.player = Player(self.screen_width, self.screen_height)
        self.clock = pygame.time.Clock()
        self.score = Score()
        # - Hold enemies, clouds in Sprite Groups
        # - All sprites group used for rendering
        self.enemy = pygame.sprite.Group()
        self.cloud = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.score)
        #defining new user event for the game - enemy generation
        self.game_event = pygame.USEREVENT + 1
        # setting the timer after which this event triggers
        pygame.time.set_timer(self.game_event, 250)
        # event for cloud creation
        self.cloud_event = pygame.USEREVENT + 2
        pygame.time.set_timer(self.cloud_event, 1000)
        self.counter = 0
        self.color_palette = [[135, 206, 250],
                              [200, 100, 100],
                              [100, 200, 50],
                              [100, 100, 200]]

    def start_loop(self):
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
                elif event.type == self.game_event:
                    new_enemy = Enemy(self.screen_width, self.screen_height)
                    self.enemy.add(new_enemy)
                    self.all_sprites.add(new_enemy)
                elif event.type == self.cloud_event:
                    new_cloud = Cloud(self.screen_width, self.screen_height)
                    self.cloud.add(new_cloud)
                    self.all_sprites.add(new_cloud)

            pressed_keys = pygame.key.get_pressed()
            self.player.update(pressed_keys)
            self.enemy.update()
            self.cloud.update()
            # self.screen.fill([135, 206, 250])
            self.screen.fill(self.color_palette[int((self.counter / 10) / 50)])
            # Draw one surface on top of another
            for sprite in self.all_sprites:
                self.screen.blit(sprite.surface, sprite.rect)
            self.score.increment_value(jump=2)
            score = self.score.font.render("Score: {0}".format(self.score.get_value()), True, (0, 0, 0))
            self.screen.blit(score, (20, 20))
            # Check for collision
            if pygame.sprite.spritecollideany(self.player, self.enemy):
                self.player.kill()
                running = False
            pygame.display.flip()
            # to ensure the game maintains a frame rate of 30
            self.clock.tick(30)
            self.counter += 1

        pygame.quit()


if __name__ == '__main__':
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 1000
    NAME = "AIR FORCE ONE"
    game = Game(name=NAME,
                screen_width=SCREEN_WIDTH,
                screen_height=SCREEN_HEIGHT)
    game.start_loop()

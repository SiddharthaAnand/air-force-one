import random
import pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super(Score, self).__init__()
        self.name = "Score: "
        self.surface = pygame.Surface((10, 10))
        # self.surface.fill((0, 255, 255))
        self.rect = self.surface.get_rect()
        self.surface.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surface.get_rect()
        self.font = pygame.font.SysFont("Courier", 20)
        # The color of the background image which pygame will
        # render as transparent since that is the background
        # color of the image/missile




class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surface = pygame.image.load('assets/cloud.png').convert()
        self.surface.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surface.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.left < 0:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
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
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Defining a Player Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surface = pygame.image.load("assets/jet.png").convert()
        self.surface.set_colorkey((255, 255, 255), RLEACCEL)
        # load image for player

        # use this to draw a player later
        self.rect = self.surface.get_rect()

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
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Game(object):
    def __init__(self, name=None, screen=None, screen_width=500, screen_height=500):
        """Initialization"""
        self.name = name
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        pygame.init()
        self.player = Player()
        self.clock = pygame.time.Clock()
        self.score = Score()
        self.text = self.score.font.render(self.score.name, True, (255, 255, 255))
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




    def create_window(self):
        """Create a sample window where the game will run."""

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
                elif event.type == self.game_event:
                    new_enemy = Enemy()
                    self.enemy.add(new_enemy)
                    self.all_sprites.add(new_enemy)
                elif event.type == self.cloud_event:
                    new_cloud = Cloud()
                    self.cloud.add(new_cloud)
                    self.all_sprites.add(new_cloud)
                # self.text_surface.font.render('1234')

            pressed_keys = pygame.key.get_pressed()
            self.player.update(pressed_keys)
            self.enemy.update()
            self.cloud.update()
            self.screen.fill([135, 206, 250])

            # Draw one surface on top of another
            for sprite in self.all_sprites:
                self.screen.blit(sprite.surface, sprite.rect)
            score = self.score.font.render("Score: {0}".format(int(self.counter / 10)), True, (0, 0, 0))
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

    @staticmethod
    def get_random_color():
        import random
        return random.randint(1, 255)


if __name__ == '__main__':
    window = Game('air-force-one', 500, 500)
    window.start_game_loop()

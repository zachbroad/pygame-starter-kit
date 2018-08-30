import pygame
import config


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(config.TITLE)
        self.screen = pygame.display.set_mode((config.X, config.Y))
        self.running = True

        # Start main game loop
        self.loop()

    def loop(self):
        while self.running:
            self.check_events()
            self.render()
            self.update()

    def render(self):
        self.screen.fill(config.COLOR)
        pygame.display.update()

    def update(self):
        pass

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


if __name__ == "__main__":
    game = Game()

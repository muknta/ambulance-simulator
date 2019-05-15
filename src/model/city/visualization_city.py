from abc import ABCMeta, abstractmethod
import pygame
from src.model.singleton import SingletonMeta

WINDOW_TITLE = "Ambulance Car On The City"
WIDTH = 800
HEIGHT = 600
FPS = 40


class Drawer:
    def draw(self): pass


class GameChanger:
    def update(self): pass


class Game(ABC, Drawer, GameChanger):
    done = False
    color_bg = pygame.Color('darkgrey')

    @abstractmethod
    def main_loop(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def handle_events(self):
        pass

    @abstractmethod
    def update(self):
        pass


class VisualCity(Game, metaclass=SingletonMeta):
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)

        self.clock = pygame.time.Clock()
        self.limit_fps = True
        self.now = 0

    def main_loop(self):
        while not self.done:
            self.handle_events()
            self.update()
            self.draw()

            if self.limit_fps:
                self.clock.tick(FPS)
            else:
                self.clock.tick()

    def draw(self):
        self.screen.fill(self.color_bg)
        pygame.display.flip()

    def update(self):
        self.now = pygame.time.get_ticks()

    def handle_events(self):
        events = pygame.event.get()
        kmods = pygame.key.get_mods()

        for event in events:
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.done = True


if __name__ == "__main__":
    visual_city = VisualCity()
    visual_city.main_loop()

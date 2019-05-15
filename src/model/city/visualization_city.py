from abc import ABC, abstractmethod
import pygame
from src.model.singleton import Singleton

WINDOW_TITLE = "Ambulance Car On The City"
WIDTH = 800
HEIGHT = 600
FPS = 60


class Drawer(ABC):
    @abstractmethod
    def draw(self):
        pass


class Handler(ABC):
    @abstractmethod
    def handle_events(self):
        pass


class Updater(ABC):
    @abstractmethod
    def update(self):
        pass


class Game(ABC):
    done = False
    color_bg = pygame.Color('darkgrey')

    @abstractmethod
    def main_loop(self):
        pass


class VisualCity(Singleton, Game, Drawer, Handler, Updater):
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)

        self.clock = pygame.time.Clock()

    def main_loop(self):
        while not self.done:
            self.handle_events()

            self.update()

            self.draw()

            self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(self.color_bg)
        pygame.display.flip()

    def update(self):
        pass

    def handle_events(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.done = True


if __name__ == "__main__":
    visual_city = VisualCity()
    visual_city.main_loop()

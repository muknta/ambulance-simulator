import pygame
from pygame.locals import *


class Map(object):
    def __init__(self, city):
        self.city = city
        self.screen = city.screen


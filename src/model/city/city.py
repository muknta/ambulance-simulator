import pygame
from pygame.locals import *

import numpy as np
import os


class Map(object):
    def __init__(self, city):
        self.city = city
        self.screen = city.screen


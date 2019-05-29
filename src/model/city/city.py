import pygame
import sys
import os


class Map(object):
    def __init__(self, city):
        self.city = city
        self.screen = city.screen


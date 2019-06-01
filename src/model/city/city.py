import pygame


class Map(object):
    def __init__(self, screen):
        self.screen = screen
        self.city_map = self.__load_map("city_matrix.txt")
        self.__draw_city(self.city_map)

    @staticmethod
    def __load_map(name):
        fullname = "img/" + name
        with open(fullname, 'r') as map_file:
            city_map = []
            for line in map_file:
                line = line.strip()
                city_map.append(line)

        return city_map

    def __draw_city(self, city_map):
        for y in range(len(city_map)):
            for x in range(len(city_map[y])):
                if city_map[y][x] == "1":
                    self.screen.fill(pygame.Color("gray"), pygame.Rect(16 * x, 16 * y, 16, 16))
                elif city_map[y][x] == "0":
                    self.screen.fill(pygame.Color("green"), pygame.Rect(16 * x, 16 * y, 16, 16))
                elif city_map[y][x] == "h":
                    self.screen.fill(pygame.Color("red"), pygame.Rect(16 * x, 16 * y, 16, 16))
                elif city_map[y][x] == "c":
                    self.screen.fill(pygame.Color("blue"), pygame.Rect(16 * x, 16 * y, 16, 16))
                elif city_map[y][x] == "q":
                    self.screen.fill(pygame.Color("brown"), pygame.Rect(16 * x, 16 * y, 16, 16))


import pygame
import random

# CONSTANTS
WIDTH = 320
HEIGHT = 480
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Car On City")
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Drawing

    # Render
    screen.fill((0, 0, 255))
    pygame.display.flip()

pygame.quit()

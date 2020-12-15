import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Pygame_tour")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event.key)
    pygame.display.update(())
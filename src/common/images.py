import pygame

pygame.init()
pygame.display.set_mode((1, 1), pygame.NOFRAME)

star = pygame.image.load("assets/textures/star.png").convert_alpha()

pygame.display.quit()
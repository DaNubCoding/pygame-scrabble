import pygame

from src.common.exe import pathof

pygame.init()
pygame.display.set_mode((1, 1), pygame.NOFRAME)

TEX = "assets/textures/"

star = pygame.image.load(pathof(f"{TEX}star.png")).convert_alpha()

pygame.display.quit()
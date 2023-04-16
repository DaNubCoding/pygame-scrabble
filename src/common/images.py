import pygame

from src.common.exe import pathof

def load_image(filename: str, scale: float = 1) -> pygame.SurfaceType:
    return pygame.transform.smoothscale_by(pygame.image.load(pathof(f"assets/textures/{filename}")).convert_alpha(), scale)

pygame.init()
pygame.display.set_mode((1, 1), pygame.NOFRAME)

star = load_image("star.png")
shuffle = load_image("shuffle.png", scale=0.6)
reset = load_image("reset.png", scale=0.7)

pygame.display.quit()
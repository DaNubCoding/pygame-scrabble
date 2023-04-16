import pygame

from src.management.scene import Scene
from src.common.constants import VEC
from src.game.element import Element

class Button1(Element):
    def __init__(self, scene: Scene, rect: tuple[float, float, float, float], image: pygame.SurfaceType) -> None:
        super().__init__(scene, rect)
        self.image = image

    def update(self) -> None:
        pass

    def draw(self) -> None:
        rect = pygame.draw.rect(self.manager.screen, self.bg_color, (VEC(self.rect.topleft) + (self.parent.rect.topleft if self.parent else (0, 0)), self.rect.size), 0, self.border_radius)
        pygame.draw.rect(self.manager.screen, self.bg_color, (rect.left - 5, rect.top - 5, rect.width + 10, rect.height + 10), 2, self.border_radius + 4)
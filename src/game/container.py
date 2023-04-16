import pygame

from src.management.scene import Scene
from src.common.constants import VEC
from src.game.element import Element

class Container(Element):
    def __init__(self, scene: Scene, rect: tuple[float, float, float, float]) -> None:
        super().__init__(scene, rect)
        self.children: list[Element] = []

    def draw(self) -> None:
        pygame.draw.rect(self.manager.screen, self.bg_color, (VEC(self.rect.topleft) + (self.parent.rect.topleft if self.parent else (0, 0)), self.rect.size), 0, self.border_radius)

    def add_children(self, *children: tuple[Element]) -> None:
        for child in children:
            child.parent = self
            child.parse_rect()
            self.children.append(child)
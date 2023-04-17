import pygame

from src.management.element import Element
from src.management.scene import Scene

class Container(Element):
    def __init__(self, scene: Scene, rect: tuple[float, float, float, float]) -> None:
        super().__init__(scene, rect)
        self.children: list[Element] = []

    def draw(self) -> None:
        pygame.draw.rect(self.manager.screen, self.bg_color, self.rect, 0, self.border_radius)

    def add_children(self, *children: tuple[Element]) -> None:
        for child in children:
            child.parent = self
            child.parse_rect()
            self.children.append(child)

Spacer = Container
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from management.container import Container

from typing import Optional
from math import ceil
import pygame

from src.management.sprite import Sprite, Layers
from src.common.constants import VEC, Color
from src.management.scene import Scene

class Style(dict):
    def __init__(self, **styles) -> None:
        for name, value in styles.items():
            self[name] = value

class Element(Sprite):
    def __init__(self, scene: Scene, rect: tuple[float, float, float, float]) -> None:
        super().__init__(scene, Layers.GUI)
        self.parent: Optional[Container] = None
        self.rect_settings = list(rect)
        try:
            self.rect = pygame.Rect(rect)
        except TypeError:
            pass

        self.bg_color = Color.BG.value
        self.border_radius = 0

    def setup(self, **styles) -> None:
        for name, value in styles.items():
            setattr(self, name, value)

    def parse_rect(self) -> None:
        self.rect = []
        self.index = self.parent.children.index(self)

        for i, value in enumerate(self.rect_settings):
            if not isinstance(value, str):
                self.rect.append(value)
                continue

            value = value.replace("p", "")

            if self.index > 0:
                prev_child = self.parent.children[self.index - 1]
                value = value.replace("$", f"$ + {prev_child.rect[i]}")
                if i < 2:
                    value = value.replace("$", f"$ + {prev_child.rect[i + 2]}")
                    value = value.replace("$", f"-{self.parent.rect[i]}")

            value = value.replace("$", "")
            value = value.replace("%", f" * {self.parent.rect[i]} / 100")
            self.rect.append(ceil(eval(value)))

        # Ellipses represent a value equal to the value of the other dimension counterpart
        for i in range(4):
            if self.rect[i] != ...: continue
            self.rect[i] = self.rect[i + (-1 if i & 1 else 1)]

        self.rect = pygame.Rect(VEC(self.rect[:2]) + (self.parent.rect.topleft if self.parent else (0, 0)), self.rect[2:])
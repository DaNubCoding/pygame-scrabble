from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.game.elements.rack_tile import RackTile

from functools import cached_property
from pygame.math import Vector3
from pygame.locals import *
import pygame

from src.common.constants import VEC, Color, TILE_SIZE, DROPPED_TILE_FONT
from src.management.sprite import Sprite, Layers
from src.management.scene import Scene

class DroppedTile(Sprite):
    def __init__(self, scene: Scene, pos: tuple[int, int], rack_tile: RackTile) -> None:
        super().__init__(scene, Layers.TILES)
        self.text = rack_tile.text
        self.rect = pygame.Rect(pos, (TILE_SIZE, TILE_SIZE))
        self.bg_color = Color.DROPPED_TILE.value
        self.fg_color = (0, 0, 0)
        self.edge_color = Color.DROPPED_TILE_EDGE.value
        self.border_radius = 7
        self.font = DROPPED_TILE_FONT

    @cached_property
    def image(self) -> pygame.SurfaceType:
        image = pygame.Surface(self.rect.size, SRCALPHA)
        pygame.draw.rect(image, self.bg_color, ((0, 0), self.rect.size), 0, self.border_radius)
        for i in range(5):
            edge_color = Vector3(self.edge_color) + (Vector3(self.bg_color) - self.edge_color) / 5 * i
            pygame.draw.rect(image, edge_color, ((i, i), VEC(self.rect.size) - (i * 2, i * 2)), 2, self.border_radius)

        text_surf = self.font.render(self.text, True, (255, 255, 255))
        image.blit(text_surf, (VEC(self.rect.size) - text_surf.get_size()) // 2 + (1, 1))
        text_surf = self.font.render(self.text, True, self.fg_color)
        image.blit(text_surf, (VEC(self.rect.size) - text_surf.get_size()) // 2)

        return image

    def draw(self) -> None:
        self.manager.screen.blit(self.image, self.rect)
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.game.elements.rack_tile import RackTile
    from src.game.held_tile import HeldTile

from functools import cached_property
from pygame.math import Vector3
from pygame.locals import *
import pygame

from src.common.constants import VEC, Color, TILE_SIZE, DROPPED_TILE_FONT
from src.game.elements.interactable import Interactable
from src.management.scene import Scene

class DroppedTile(Interactable):
    def __init__(self, scene: Scene, board_pos: tuple[int, int], pos: tuple[int, int], held_tile: HeldTile, rack_tile: RackTile) -> None:
        super().__init__(scene, (*pos, TILE_SIZE, TILE_SIZE))
        self.held_tile = held_tile
        self.rack_tile = rack_tile
        self.setup(
            text = rack_tile.text,
            bg_color = Color.DROPPED_TILE.value,
            fg_color = (0, 0, 0),
            edge_color = Color.DROPPED_TILE_EDGE.value,
            border_radius = 7,
            font = DROPPED_TILE_FONT,
        )
        self.board_pos = board_pos
        self.scene.board.board[int(board_pos.y) - 1][int(board_pos.x) - 1] = self.text

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

    def on_click(self) -> None:
        self.scene.board[self.board_pos] = None

        self.held_tile.offset = self.manager.mouse_pos - self.rect.topleft
        self.held_tile.scale = 0.8
        self.held_tile.revive()
        self.kill()
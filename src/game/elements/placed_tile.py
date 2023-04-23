from functools import cached_property
from pygame.math import Vector3
from pygame.locals import *
import pygame

from src.common.constants import VEC, Color, TILE_SIZE, TILE_MARGIN, PLACED_TILE_FONT
from src.management.element import Element
from src.management.scene import Scene

class PlacedTile(Element):
    def __init__(self, scene: Scene, board_pos: tuple[int, int], text: str) -> None:
        pos = VEC(board_pos) * (TILE_SIZE + TILE_MARGIN) - VEC(TILE_MARGIN, TILE_MARGIN) * 2
        super().__init__(scene, (*pos, TILE_SIZE, TILE_SIZE))

        self.text = text
        self.setup(
            text = self.text,
            bg_color = Color.PLACED_TILE.value,
            fg_color = (0, 0, 0),
            edge_color = Color.PLACED_TILE_EDGE.value,
            border_radius = 7,
            font = PLACED_TILE_FONT,
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
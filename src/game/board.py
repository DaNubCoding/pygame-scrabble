from functools import cached_property
from typing import Generator
from pygame.locals import *
import pygame

from src.common.constants import VEC, Color, TILE_SIZE, TILE_MARGIN, BONUS_LOCATIONS, BONUS_FONT, AXIS_FONT, BOARD_SIZE, NUM_TILES
from src.management.sprite import Sprite, Layers
from src.management.container import Container
from src.management.element import Element
from src.management.scene import Scene
from src.common.utils import inttup
import src.common.images as images

class Board(Container):
    def __init__(self, scene: Scene) -> None:
        super().__init__(scene, (40, 40, BOARD_SIZE, BOARD_SIZE))
        self._board = [[None] * NUM_TILES for _ in range(NUM_TILES)]

        for x in range(NUM_TILES):
            for y in range(NUM_TILES):
                BoardTile(self.scene, self, (x, y))

    def draw(self) -> None:
        self.draw_axes()

    def draw_axes(self) -> None:
        for i in range(15):
            text_surf = AXIS_FONT.render(chr(65 + i), True, Color.AXIS_TEXT.value)
            self.manager.screen.blit(text_surf, (self.rect.left + 18 + i * (TILE_SIZE + TILE_MARGIN), self.rect.top - 18))

        for i in range(15):
            text_surf = AXIS_FONT.render(f"{i + 1: >2}", True, Color.AXIS_TEXT.value)
            self.manager.screen.blit(text_surf, (self.rect.left - 20, self.rect.top + 16 + i * (TILE_SIZE + TILE_MARGIN)))

class BoardTile(Element):
    def __init__(self, scene: Scene, board: Board, pos: tuple[int, int]) -> None:
        super().__init__(scene, (*(VEC(pos) * (TILE_SIZE + TILE_MARGIN)), TILE_SIZE, TILE_SIZE))
        self.pos = VEC(pos)
        self.parent = board
        self.parent.add_children(self)

    @cached_property
    def image(self) -> pygame.SurfaceType:
        image = pygame.Surface((TILE_SIZE, TILE_SIZE), SRCALPHA)
        color = BONUS_LOCATIONS[inttup(self.pos + (1, 1))] if inttup(self.pos + (1, 1)) in BONUS_LOCATIONS else Color.TILE_BG
        pygame.draw.rect(image, color.value, (0, 0, TILE_SIZE, TILE_SIZE), 0, 7)
        if color != Color.TILE_BG:
            if self.pos == (7, 7):
                image.blit(images.star, (0, 0))
            else:
                text_surf = BONUS_FONT.render(color.name, True, (255, 255, 255))
                image.blit(text_surf, (VEC(TILE_SIZE) - text_surf.get_size()) // 2)
        return image

    def draw(self) -> None:
        self.manager.screen.blit(self.image, self.rect)
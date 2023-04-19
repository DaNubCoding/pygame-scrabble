from typing import Generator
import pygame

from src.common.constants import VEC, Color, TILE_SIZE, TILE_MARGIN, BONUS_LOCATIONS, BONUS_FONT, AXIS_FONT
from src.management.sprite import Sprite, Layers
from src.management.scene import Scene
import src.common.images as images

class Board(Sprite):
    def __init__(self, scene: Scene) -> None:
        super().__init__(scene, Layers.GUI)
        self._board = [[None] * 15 for _ in range(15)]
        self.topleft = VEC(40, 40)

    def update(self) -> None:
        super().update()

    def draw(self) -> None:
        self.draw_board()
        self.draw_axes()

    def draw_board(self) -> None:
        for x, y, tile in self.board:
            pos = VEC(self.topleft.x + x * (TILE_SIZE + TILE_MARGIN), self.topleft.y + y * (TILE_SIZE + TILE_MARGIN))
            color = BONUS_LOCATIONS[(x + 1, y + 1)] if (x + 1, y + 1) in BONUS_LOCATIONS else Color.TILE_BG
            pygame.draw.rect(self.manager.screen, color.value, (*pos, TILE_SIZE, TILE_SIZE), 0, 7)
            if color != Color.TILE_BG:
                if (x, y) == (7, 7):
                    self.manager.screen.blit(images.star, pos)
                    continue
                text_surf = BONUS_FONT.render(color.name, True, (255, 255, 255))
                self.manager.screen.blit(text_surf, pos + (VEC(TILE_SIZE) - text_surf.get_size()) // 2)

    def draw_axes(self) -> None:
        for i in range(15):
            text_surf = AXIS_FONT.render(chr(65 + i), True, Color.AXIS_TEXT.value)
            self.manager.screen.blit(text_surf, (self.topleft.x + 18 + i * (TILE_SIZE + TILE_MARGIN), self.topleft.y - 18))

        for i in range(15):
            text_surf = AXIS_FONT.render(f"{i + 1: >2}", True, Color.AXIS_TEXT.value)
            self.manager.screen.blit(text_surf, (self.topleft.x - 20, self.topleft.y + 16 + i * (TILE_SIZE + TILE_MARGIN)))

    @property
    def board(self) -> Generator:
        for y, row in enumerate(self._board):
            for x, tile in enumerate(row):
                yield x, y, tile
from typing import Generator
import pygame

from src.common.constants import Color, TILE_SIZE, TILE_MARGIN, BONUS_LOCATIONS
from src.management.scene import Scene

class MainGame(Scene):
    def setup(self) -> None:
        super().setup()
        self._board = [[None] * 15 for _ in range(15)]

    def update(self) -> None:
        super().update()

    def draw(self) -> None:
        self.manager.screen.fill(Color.BG.value)
        for x, y, tile in self.board:
            pos = 40 + x * (TILE_SIZE + TILE_MARGIN), 40 + y * (TILE_SIZE + TILE_MARGIN)
            color = BONUS_LOCATIONS[(x + 1, y + 1)] if (x + 1, y + 1) in BONUS_LOCATIONS else Color.TILE_BG
            pygame.draw.rect(self.manager.screen, color.value, (*pos, TILE_SIZE, TILE_SIZE), 0, 6)
        super().draw()

    @property
    def board(self) -> Generator:
        for y, row in enumerate(self._board):
            for x, tile in enumerate(row):
                yield x, y, tile
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.game.elements.dropped_tile import DroppedTile
    from src.game.elements.rack_tile import RackTile

from math import ceil
import pygame

from src.common.constants import VEC, TILE_SIZE, TILE_MARGIN
from src.game.elements.dropped_tile import DroppedTile
from src.management.sprite import Sprite, Layers
from src.management.scene import Scene
from src.common.utils import ceilvec

class HeldTile(Sprite):
    def __init__(self, scene: Scene, pos: tuple[int, int], rack_tile: RackTile) -> None:
        super().__init__(scene, Layers.TILES)
        self.rack_tile = rack_tile
        self.image = self.rack_tile.image
        self.scale = 1
        self.pos = VEC(pos)
        self.offset = self.manager.mouse_pos - self.pos

    def update(self) -> None:
        if self.manager.mouse_state[0]:
            self.pos = self.manager.mouse_pos - self.offset
        else:
            self.drop()

    def drop(self) -> None:
        rect, m_pos = self.scene.rack.rect, self.manager.mouse_pos
        if rect.left < m_pos.x < rect.right and rect.top < m_pos.y < rect.bottom:
            self.drop_on_rack()

        self.board_pos = ceilvec((self.manager.mouse_pos - self.scene.board.rect.topleft) / (TILE_SIZE + TILE_MARGIN))
        if not 1 <= self.board_pos.x <= 15 or not 1 <= self.board_pos.y <= 15:
            self.withdraw()
            return

        if not self.scene.board[self.board_pos]:
            self.drop_on_board()
            return
        self.withdraw()

    def drop_on_rack(self) -> None:
        self.scene.rack.children.insert(self.scene.rack.children.index(self.rack_tile), None) # Insert placeholder
        self.scene.rack.children.remove(self.rack_tile)

        tile_width = self.scene.rack.rect.width / 7
        index = ceil((self.manager.mouse_pos.x - self.scene.rack.rect.left + tile_width // 2) / tile_width)
        self.scene.rack.children.insert(index, self.rack_tile)
        self.scene.rack.children.remove(None) # Remove placeholder

        self.scene.reorder_rack()

    def drop_on_board(self) -> None:
        DroppedTile(self.scene, self.board_pos, self, self.rack_tile)
        self.kill()

    def withdraw(self) -> None:
        self.scene.sprite_manager.add(self.rack_tile)
        self.kill()

    def draw(self) -> None:
        self.manager.screen.blit(pygame.transform.scale_by(self.image, self.scale), self.pos)

    def revive(self) -> None:
        self.scene.sprite_manager.add(self)
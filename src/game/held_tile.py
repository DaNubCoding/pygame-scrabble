from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.game.elements.rack_tile import RackTile

from math import ceil

from src.common.constants import VEC, TILE_SIZE, TILE_MARGIN
from src.management.sprite import Sprite, Layers
from src.game.dropped_tile import DroppedTile
from src.management.scene import Scene
from src.common.utils import ceilvec

class HeldTile(Sprite):
    def __init__(self, scene: Scene, pos: tuple[int, int], rack_tile: RackTile) -> None:
        super().__init__(scene, Layers.TILES)
        self.rack_tile = rack_tile
        self.image = self.rack_tile.image
        self.pos = VEC(pos)
        self.offset = self.manager.mouse_pos - self.pos

    def update(self) -> None:
        if self.manager.mouse_state[0]:
            self.pos = self.manager.mouse_pos - self.offset
        else:
            self.drop()

    def drop(self) -> None:
        # On rack
        children, rect, m_pos = self.scene.rack.children, self.scene.rack.rect, self.manager.mouse_pos
        if rect.left < m_pos.x < rect.right and rect.top < m_pos.y < rect.bottom:
            children.insert(children.index(self.rack_tile), None) # Insert placeholder
            children.remove(self.rack_tile)

            tile_width = rect.width / 7
            children.insert(ceil((m_pos.x - rect.left + tile_width // 2) / tile_width), self.rack_tile)
            children.remove(None) # Remove placeholder

            self.scene.reorder_rack()

        # Out of board
        board_pos = ceilvec((self.manager.mouse_pos - self.scene.board.rect.topleft) / (TILE_SIZE + TILE_MARGIN))
        if not 1 <= board_pos.x <= 15 or not 1 <= board_pos.y <= 15:
            self.withdraw()
            return

        # On board
        pos = board_pos * (TILE_SIZE + TILE_MARGIN) - VEC(TILE_MARGIN, TILE_MARGIN) * 2
        DroppedTile(self.scene, pos, self.rack_tile)
        self.rack_tile.kill()
        self.kill()

    def withdraw(self) -> None:
        self.scene.sprite_manager.add(self.rack_tile)
        self.kill()

    def draw(self) -> None:
        self.manager.screen.blit(self.image, self.pos)
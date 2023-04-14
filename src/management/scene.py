from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.management.manager import GameManager

from src.management.sprite import SpriteManager

class Scene:
    def __init__(self, manager: GameManager, previous_scene: Scene) -> None:
        self.manager = manager
        self.previous_scene = previous_scene
        self.sprite_manager = SpriteManager(self)

    def setup(self) -> None:
        self.sprite_manager = SpriteManager(self)

    def update(self) -> None:
        self.sprite_manager.update()

    def draw(self) -> None:
        self.sprite_manager.draw()
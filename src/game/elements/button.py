from typing import Callable, Any
import pygame

from src.game.elements.interactable import Interactable
from src.game.elements.dropped_tile import DroppedTile
from src.common.constants import VEC, Color
from src.management.scene import Scene
import src.common.images as images

class Button(Interactable):
    def __init__(self, scene: Scene, rect: tuple[float, float, float, float], command: Callable) -> None:
        super().__init__(scene, rect)
        self.command = command

    def setup(self, **kwargs) -> None:
        # Ensure default colors
        self.idle_color = self.hover_color = self.click_color = Color.BG.value
        self.idle_fg_color = (0, 0, 0)
        super().setup(**kwargs)
        # Ensure an initial background color
        self.bg_color = self.idle_color
        self.fg_color = self.idle_fg_color

    def on_hover(self) -> None:
        self.bg_color = self.hover_color

    def on_click(self) -> None:
        self.bg_color = self.click_color
        self.command()

    def off_hover(self) -> None:
        self.bg_color = self.idle_color

    def off_click(self) -> None:
        self.bg_color = self.hover_color

class ButtonType1(Button):
    """Used by all options buttons and is superclass to ShuffleButton and ResetButton"""
    def __init__(self, scene: Scene, rect: tuple[float, float, float, float], command: Callable[..., None]) -> None:
        super().__init__(scene, rect, command)
        self.image = None
        self.text = None

    def draw(self) -> None:
        pygame.draw.rect(self.manager.screen, (255, 255, 255), self.rect, 0, self.border_radius + 4)
        pygame.draw.rect(self.manager.screen, self.bg_color, self.rect, 1, self.border_radius + 4)
        pygame.draw.rect(self.manager.screen, self.bg_color, (VEC(self.rect.topleft) + (5, 5), VEC(self.rect.size) - (10, 10)), 0, self.border_radius)
        if self.image:
            self.manager.screen.blit(self.image, (VEC(self.rect.topleft) + (VEC(self.rect.size) - self.image.get_size()) // 2))
        elif self.text:
            text_surf = self.font.render(self.text, True, self.fg_color)
            self.manager.screen.blit(text_surf, VEC(self.rect.topleft) + (VEC(self.rect.size) - text_surf.get_size()) // 2)

class ResetButton(ButtonType1):
    """The reset/clear button"""
    def __init__(self, scene: Scene, rect: tuple[float, float, float, float]) -> None:
        super().__init__(scene, rect, scene.reset)
        self.image = images.reset
        self.border_radius = 12

    def update(self) -> None:
        if not DroppedTile._registry:
            self.to_reset()
        else:
            self.to_clear()

        super().update()

    def to_reset(self) -> None:
        self.image = images.reset
        self.command = self.scene.reset

    def to_clear(self) -> None:
        self.image = images.clear
        self.command = self.scene.clear

class ShuffleButton(ButtonType1):
    """The shuffle button"""
    def __init__(self, scene: Scene, rect: tuple[float, float, float, float]) -> None:
        super().__init__(scene, rect, scene.shuffle)
        self.image = images.shuffle
        self.border_radius = 12

    def update(self) -> None:
        self.locked = bool(DroppedTile._registry)
        if self.locked:
            self.bg_color = self.hover_color

        super().update()
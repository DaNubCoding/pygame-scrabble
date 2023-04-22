from typing import Callable
import pygame

from src.game.elements.interactable import Interactable
from src.common.constants import VEC, Color
from src.management.scene import Scene

class Button(Interactable):
    def __init__(self, scene: Scene, rect: tuple[float, float, float, float], command: Callable) -> None:
        super().__init__(scene, rect)
        self.command = command

    def setup(self, **kwargs) -> None:
        # Ensure default colors
        self.idle_color = self.hover_color = self.click_color = Color.BG.value
        super().setup(**kwargs)
        # Ensure an initial background color
        self.bg_color = self.idle_color

    def on_hover(self) -> None:
        self.bg_color = self.hover_color

    def on_click(self) -> None:
        self.bg_color = self.click_color
        self.command()

    def off_hover(self) -> None:
        self.bg_color = self.idle_color

    def off_click(self) -> None:
        self.bg_color = self.hover_color

class Button1(Button):
    def __init__(self, scene: Scene, rect: tuple[float, float, float, float], command: Callable) -> None:
        super().__init__(scene, rect, command)
        self.image = None
        self.text = None
        self.font = None

    def draw(self) -> None:
        pygame.draw.rect(self.manager.screen, (255, 255, 255), self.rect, 0, self.border_radius + 4)
        pygame.draw.rect(self.manager.screen, self.bg_color, self.rect, 1, self.border_radius + 4)
        pygame.draw.rect(self.manager.screen, self.bg_color, (VEC(self.rect.topleft) + (5, 5), VEC(self.rect.size) - (10, 10)), 0, self.border_radius)
        if self.image:
            self.manager.screen.blit(self.image, (VEC(self.rect.topleft) + (VEC(self.rect.size) - self.image.get_size()) // 2))
        elif self.text:
            text_surf = self.font.render(self.text, True, self.fg_color)
            self.manager.screen.blit(text_surf, VEC(self.rect.topleft) + (VEC(self.rect.size) - text_surf.get_size()) // 2)
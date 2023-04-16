from typing import Callable
import pygame

from src.common.constants import VEC, Color, OPTIONS_BUTTON_FONT
from src.game.interactable import Interactable
from src.management.scene import Scene

class Button1(Interactable):
    def __init__(self, scene: Scene, rect: tuple[float, float, float, float], image: pygame.SurfaceType, command: Callable) -> None:
        super().__init__(scene, rect)
        self.image = image
        self.command = command

    def draw(self) -> None:
        pygame.draw.rect(self.manager.screen, self.bg_color, self.rect, 0, self.border_radius)
        pygame.draw.rect(self.manager.screen, self.bg_color, (VEC(self.rect.topleft) - (5, 5), VEC(self.rect.size) + (10, 10)), 2, self.border_radius + 4)
        self.manager.screen.blit(self.image, (VEC(self.rect.topleft) + (VEC(self.rect.size) - self.image.get_size()) // 2))

    def on_hover(self) -> None:
        self.bg_color = Color.RACK_BUTTON_HOVER.value

    def on_click(self) -> None:
        self.bg_color = Color.RACK_BUTTON_CLICK.value
        self.command()

    def off_hover(self) -> None:
        self.bg_color = Color.RACK_BUTTON_IDLE.value

    def off_click(self) -> None:
        self.bg_color = Color.RACK_BUTTON_HOVER.value

class Button2(Interactable):
    def __init__(self, scene: Scene, rect: tuple[float, float, float, float], text: str, command: Callable) -> None:
        super().__init__(scene, rect)
        self.text = text
        self.command = command

    def draw(self) -> None:
        pygame.draw.rect(self.manager.screen, (255, 255, 255), self.rect, 0, self.border_radius + 4)
        pygame.draw.rect(self.manager.screen, self.bg_color, (VEC(self.rect.topleft) + (4, 4), VEC(self.rect.size) - (8, 8)), 0, self.border_radius)
        text_surf = OPTIONS_BUTTON_FONT.render(self.text, True, self.fg_color)
        self.manager.screen.blit(text_surf, VEC(self.rect.topleft) + (VEC(self.rect.size) - text_surf.get_size()) // 2)
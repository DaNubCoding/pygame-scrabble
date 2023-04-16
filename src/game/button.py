from typing import Callable
import pygame

from src.game.interactable import Interactable
from src.common.constants import VEC, Color
from src.management.scene import Scene

class Button1(Interactable):
    def __init__(self, scene: Scene, rect: tuple[float, float, float, float], image: pygame.SurfaceType, command: Callable) -> None:
        super().__init__(scene, rect)
        self.image = image
        self.command = command

    def draw(self) -> None:
        rect = pygame.draw.rect(self.manager.screen, self.bg_color, self.rect, 0, self.border_radius)
        pygame.draw.rect(self.manager.screen, self.bg_color, (rect.left - 5, rect.top - 5, rect.width + 10, rect.height + 10), 2, self.border_radius + 4)
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